import os

from pages.products_page import ProductsPage

import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()

@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    return page


@pytest.fixture
def cart_ready_page(logged_in_page):
    page = logged_in_page

    product = ProductsPage(page)
    product.add_product_to_cart("Sauce Labs Backpack")
    product.open_cart()
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")

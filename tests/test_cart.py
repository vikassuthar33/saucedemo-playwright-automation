import pytest

from conftest import cart_ready_page

from playwright.sync_api import expect, Page
from pages.cart_page import CartPage

@pytest.mark.smoke
@pytest.mark.regression
def test_cart_page_load(cart_ready_page: Page):
    page = cart_ready_page
    cart = CartPage(page)

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart.title).to_have_text("Your Cart")

@pytest.mark.regression
def test_product_is_visible_in_cart(cart_ready_page: Page):
    page = cart_ready_page
    product_name = "Sauce Labs Backpack"
    # verify product present
    expect(page.locator(".cart_item").filter(has_text=product_name)).to_have_count(1)

@pytest.mark.regression
def test_remove_product_from_cart(cart_ready_page: Page):
    page = cart_ready_page
    product_name = "Sauce Labs Backpack"
    cart = CartPage(page)

    # remove product
    cart.remove_product(product_name)

    # verify removed
    expect(page.locator(".cart_item").filter(has_text=product_name)).to_have_count(0)

@pytest.mark.smoke
@pytest.mark.regression
def test_continue_shopping_navigation(cart_ready_page: Page):
    page = cart_ready_page
    cart = CartPage(page)
    cart.click_continue_shopping()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_checkout_navigation(cart_ready_page: Page):
    page = cart_ready_page
    cart = CartPage(page)
    cart.click_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")


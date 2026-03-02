
from playwright.sync_api import expect

from pages.login_page import LoginPage

from config.test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD
)

def test_valid_login(page):
    login = LoginPage(page)

    login.open()
    login.login(VALID_USERNAME, VALID_PASSWORD)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_invalid_login(page):
    login = LoginPage(page)
    login.open()
    login.login(INVALID_USERNAME, INVALID_PASSWORD)

    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")

def test_login_without_credentials(page):
    login = LoginPage(page)
    login.open()
    login.click_login()
    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_contain_text("Epic sadface: Username is required")
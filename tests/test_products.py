
from conftest import page


from playwright.sync_api import expect
from pages.products_page import ProductsPage
from config.test_data import DEFAULT_PRODUCT

def test_product_title(logged_in_page, page):
    page = logged_in_page
    inventory = ProductsPage(page)

    expect(inventory.title).to_have_text("Products")

def test_products_present(logged_in_page, page):
    page = logged_in_page
    inventory = ProductsPage(page)
    count = inventory.get_product_count()
    assert count > 0

def test_add_to_cart(logged_in_page, page):
    page = logged_in_page
    inventory = ProductsPage(page)

    inventory.add_product_to_cart(DEFAULT_PRODUCT)

    # badge should be 1
    expect(inventory.cart_badge).to_have_text("1")

def test_remove_from_cart(logged_in_page, page):
    page = logged_in_page
    inventory = ProductsPage(page)

    inventory.add_product_to_cart(DEFAULT_PRODUCT)
    expect(inventory.cart_badge).to_have_text("1")

    inventory.remove_product_from_cart(DEFAULT_PRODUCT)
    expect(inventory.cart_badge).to_have_count(0)

def test_sort_price_low_to_high(logged_in_page, page):
    page = logged_in_page
    inventory = ProductsPage(page)

    inventory.sort("lohi")
    prices = inventory.get_all_prices()

    assert prices == sorted(prices), f"Prices not sorted low-high: {prices}"

def test_sort_name_a_to_z(logged_in_page, page):
    page = logged_in_page
    inventory = ProductsPage(page)

    inventory.sort("az")
    names = inventory.get_all_names()

    assert names == sorted(names), f"Names not sorted A-Z: {names}"


def test_open_cart(logged_in_page, page):
    page = logged_in_page
    inventory = ProductsPage(page)

    inventory.add_product_to_cart(DEFAULT_PRODUCT)
    inventory.open_cart()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")



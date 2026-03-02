
from playwright.sync_api import expect, Page
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_step_one_navigation(logged_in_page: Page):
    page = logged_in_page
    product_name = "Sauce Labs Backpack"

    # add product + go cart
    inventory = ProductsPage(page)
    inventory.add_product_to_cart(product_name)
    inventory.open_cart()

    # cart -> checkout
    cart = CartPage(page)
    cart.click_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")


def test_checkout_step_one_required_fields(logged_in_page: Page):
    page = logged_in_page
    product_name = "Sauce Labs Backpack"

    # add product + go cart
    inventory = ProductsPage(page)
    inventory.add_product_to_cart(product_name)
    inventory.open_cart()

    cart = CartPage(page)
    cart.click_checkout()

    checkout = CheckoutPage(page)

    # click continue without entering info
    checkout.click_continue()

    # verify error
    expect(page.locator("[data-test='error']")).to_be_visible()
    expect(page.locator("[data-test='error']")).to_contain_text("First Name is required")


def test_checkout_complete_flow(logged_in_page: Page):
    page = logged_in_page
    product_name = "Sauce Labs Backpack"

    # add product + go cart
    inventory = ProductsPage(page)
    inventory.add_product_to_cart(product_name)
    inventory.open_cart()

    cart = CartPage(page)
    cart.click_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    # step one
    checkout = CheckoutPage(page)
    checkout.fill_checkout_info("John", "Doe", "120120")
    checkout.click_continue()

    # step two (overview)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(checkout.title).to_have_text("Checkout: Overview")

    assert checkout.get_cart_item_count() > 0

    expect(checkout.summary_info).to_be_visible()
    expect(checkout.subtotal).to_be_visible()
    expect(checkout.tax).to_be_visible()
    expect(checkout.total).to_be_visible()

    # finish
    checkout.click_finish()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    # back home
    checkout.click_back_home()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


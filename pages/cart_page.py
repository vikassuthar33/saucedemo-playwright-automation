from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page: Page = page

        # --- Locators ---
        self.title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")

        self.continue_shopping_btn = page.get_by_role("button", name="Continue Shopping")
        self.checkout_btn = page.get_by_role("button", name="Checkout")

    def get_cart_item_count(self) -> int:
        return self.cart_items.count()

    def is_product_in_cart(self, product_name: str):
        return self.page.locator(".cart_item").filter(has_text=product_name).count() > 0

    def remove_product(self, product_name: str):
        item = self.page.locator(".cart_item").filter(has_text=product_name)
        item.get_by_role("button", name="Remove").click()

    def click_continue_shopping(self):
        self.continue_shopping_btn.click()

    def click_checkout(self):
        self.checkout_btn.click()

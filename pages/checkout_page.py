from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page: Page = page

        # ---------- Step One (Your Information) ----------
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")

        self.continue_btn = page.get_by_role("button", name="Continue")
        self.cancel_btn = page.get_by_role("button", name="Cancel")

        # ---------- Step Two (Overview) ----------
        self.title = page.locator(".title")  # "Checkout: Overview"
        self.cart_items = page.locator(".cart_item")

        self.summary_info = page.locator(".summary_info")
        self.subtotal = page.locator(".summary_subtotal_label")
        self.tax = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")

        self.finish_btn = page.get_by_role("button", name="Finish")

        # ---------- Complete ----------
        self.back_home_btn = page.get_by_role("button", name="Back Home")

    # Step One: fill information and continue
    def fill_checkout_info(self, first: str, last: str, zip_code: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)

    def click_continue(self):
        self.continue_btn.click()

    def click_cancel(self):
        self.cancel_btn.click()

    # Step Two: finish
    def click_finish(self):
        self.finish_btn.click()

    # Complete page
    def click_back_home(self):
        self.back_home_btn.click()

    # Small helpers
    def get_cart_item_count(self) -> int:
        return self.cart_items.count()


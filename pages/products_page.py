
from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.add_to_cart = page.get_by_role("button", name="Add to cart")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.product_price = page.locator(".inventory_item_price")
        self.product_name = page.locator(".inventory_item_name")

    def is_products_title_visible(self):
        return self.title.is_visible()

    def get_product_count(self):
        return self.inventory_items.count()

    def add_product_to_cart(self, product_name: str):
        item = self.page.locator(".inventory_item").filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_product_from_cart(self, product_name: str):
        item = self.page.locator(".inventory_item").filter(has_text=product_name)
        item.get_by_role("button", name="remove").click()

    def open_cart(self):
        self.cart_link.click()

    def sort(self, option_value:str):
        self.sort_dropdown.select_option(option_value)

    def get_all_prices(self):
        prices_text = self.product_price.all_inner_texts()
        return [float(p.replace("$", "").strip()) for p in prices_text]

    def get_all_names(self) -> list[str]:
        return [name.strip() for name in self.product_name.all_inner_texts()]


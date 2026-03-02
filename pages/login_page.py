from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com/"

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def click_login(self):
        self.login_button.click()

    def get_error_text(self):
        return self.error_message.text_content()

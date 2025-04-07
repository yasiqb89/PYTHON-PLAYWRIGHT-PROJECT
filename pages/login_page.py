from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.error_message = page.locator("[data-test='error']")
        self.header_swaglab = page.locator("[data-test=\"primary-header\"]")

    def goto_url(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self):
        return self.error_message.inner_text()
    

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("standard_user", "secret_sauce")

    # Validate login access using text and url validation
    expect(page.locator("[data-test=\"primary-header\"]")).to_contain_text("Swag Labs")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("invalid_user", "wrong_password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")

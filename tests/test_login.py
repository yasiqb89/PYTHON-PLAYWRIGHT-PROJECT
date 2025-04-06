import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("standard_user", "secret_sauce")

    # Validate login access using text and url validation
    expect(login_page.header_swaglab).to_contain_text("Swag Labs")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("invalid_user", "wrong_password")

    # Validate using text
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_locked_out_user_login(page):
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("locked_out_user", "secret_sauce")

    # Validate using assert on text
    error_text = login_page.get_error_text()
    assert "Sorry, this user has been locked out." in error_text


@pytest.mark.parametrize("username, password, expected_error",[
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")])
def test_invalid_credentials(page: Page, username, password, expected_error):
    "Testing login page with invalid login credentials"
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login(username, password)

    #Check error message
    expect(login_page.error_message).to_be_visible()
    error_message = login_page.error_message
    expect(error_message).to_have_text(expected_error)


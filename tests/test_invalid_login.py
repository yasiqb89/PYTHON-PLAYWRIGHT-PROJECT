import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect



def test_invalid_login_password(page: Page):
    "Testing without parameters"
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("invalid_user", "wrong_password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")

@pytest.mark.parametrize("username, password, expected_error",[
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")])
def test_login_with_invalid_credentials(page:Page, username, password, expected_error):
    "Testing login page with invalid login credentials, and parameters"
    page.goto("https://www.saucedemo.com/")
    loging_page = LoginPage(page)
    loging_page.login(username, password)

    #Check error message
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_have_text(expected_error)






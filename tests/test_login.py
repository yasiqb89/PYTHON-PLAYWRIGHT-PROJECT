import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage

pytestmark = pytest.mark.login


@pytest.mark.login # Can use marker for separate tests as well, instead of whole file. 
def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    # Validate login access using text and url validation
    expect(login_page.header_swaglab).to_contain_text("Swag Labs")
    assert page.url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.login
def test_locked_out_user_login(page):
    "Testing without parametrize"
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("locked_out_user", "secret_sauce")

    # Validate using assert on text
    error_text = login_page.get_error_text()
    assert "Sorry, this user has been locked out." in error_text

def test_logout_session(page: Page):
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    navigation_page = NavigationPage(page)
    navigation_page.logout()

    # Try to go inventory page after logout
    page.goto("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_url("https://www.saucedemo.com/")
    

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import Page, expect 

def test_complete_chekout(page:Page):
    "End to End test: Login -> Add item -> Checkout -> Order confirmation"

    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart.click()

    checkout_page = CheckoutPage(page, inventory_page)
    checkout_page.proceed_to_checkout()
    checkout_page.enter_shipping_details("John", "Wick", "123")
    checkout_page.complete_checkout()
    expect(checkout_page.order_success_message).to_have_text("Thank you for your order!")

@pytest.mark.parametrize("username", ["standard_user", "standard_user", "standard_user"]) # Only these "standard_username" work on the used website
def test_complete_checkout_multiple_users(page:Page, username):
    "Testing the checkout flow with multiple users"

    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login(username, "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart.click()

    checkout_page = CheckoutPage(page, inventory_page)
    checkout_page.proceed_to_checkout()
    checkout_page.enter_shipping_details("John", "Wick", "123")
    checkout_page.complete_checkout()
    expect(checkout_page.order_success_message).to_have_text("Thank you for your order!")

@pytest.mark.parametrize("first_name, last_name, postal_code, expected_error",[
    ("", "Wick", "12345", "Error: First Name is required"),
    ("John", "", "12345", "Error: Last Name is required"),
    ("John", "Wick", "", "Error: Postal Code is required")])
def test_checkout_with_invalid_data(page:Page, first_name, last_name, postal_code, expected_error):
    "Test checkout stage with different scenarios: missing first name, last name and postal code"

    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart.click()

    checkout_page = CheckoutPage(page, inventory_page)
    checkout_page.proceed_to_checkout()
    checkout_page.enter_shipping_details(first_name, last_name, postal_code)

    #Check error message
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_have_text(expected_error)
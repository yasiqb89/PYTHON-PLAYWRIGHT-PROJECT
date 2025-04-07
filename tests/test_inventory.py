import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_inventory_page_product_list(page: Page):
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)

    # Verify the correct page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # Check a specific product is listed
    product_names = inventory_page.get_all_product_names()
    assert len(product_names) > 0
    assert "Sauce Labs Backpack" in product_names

def test_product_detail(page: Page):
    """When a user clicks a product (e.g. “Sauce Labs Backpack”),
    they are navigated to the correct product page, and the details (name, price, description) match"""
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(page)
    
    # Get product data
    expected_name = inventory_page.first_product_name.inner_text()
    expected_price = inventory_page.first_product_price.inner_text()
    expected_desc = inventory_page.first_product_desc.inner_text()
    
    inventory_page.click_first_product()
    actual_name = page.locator(".inventory_details_name").inner_text()
    actual_price = page.locator(".inventory_details_price").inner_text()
    actual_desc = page.locator(".inventory_details_desc").inner_text()

    assert actual_name == expected_name
    assert actual_price == expected_price
    assert actual_desc == expected_desc
    
def test_add_item_to_cart(page: Page):
    "Testing adding an item to the cart"
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()

def test_remove_item_from_cart(page: Page):
    "Testing remove item from cart"
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart()
    inventory_page.remove_item_from_cart()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()

def test_open_cart(page: Page):
    "Test opening the cart page"
    login_page = LoginPage(page)
    login_page.navigation()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.open_cart()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")

@pytest.mark.skip
def test_cart_total_updates_correctly(page: Page):
    login_page =  LoginPage(page)
    login_page.navigation()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_multiple_items_to_cart()
    expect(inventory_page.cart_badge).to_have_text("2")
    inventory_page.cart_button.click()


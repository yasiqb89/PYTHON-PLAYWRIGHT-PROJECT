import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.navigation_page import NavigationPage
from playwright.sync_api import Page, expect

pytestmark = pytest.mark.inventory

@pytest.mark.inventory
def test_inventory_page_product_list(page: Page):
    login_page = LoginPage(page)
    login_page.goto_url()
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
    login_page.goto_url()
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
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()

def test_remove_item_from_cart(page: Page):
    "Testing remove item from cart"
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart()
    inventory_page.remove_item_from_cart()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()

def test_open_cart(page: Page):
    "Test opening the cart page"
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.open_cart()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")


def test_cart_total_updates_correctly(page: Page):
    login_page =  LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_multiple_items_to_cart()
    expect(inventory_page.cart_badge).to_have_text("2")
    inventory_page.cart_button.click()

    checkout_page = CheckoutPage(page, inventory_page)
    checkout_page.proceed_to_checkout()
    checkout_page.enter_shipping_details("Jogn", "Wick", "123")

    # Calculate expected total at checkout step
    expected_total = inventory_page.get_cart_total()
    displayed_total = float(page.locator(".summary_subtotal_label").inner_text().split("$")[1])

    assert expected_total == displayed_total, f"Expected: {expected_total}, Got: {displayed_total}"


def test_cart_persistence_after_navigation(page: Page):
    "Test that cart remembers items after navigating away"
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack.click()
    page.goto("https://www.saucedemo.com/inventory.html")

    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.parametrize("sort_option, expected_order",[
    ("az", True), # Name A -> Z
    ("za", False), # Name Z -> A
])
def test_sort_by_name(page: Page, sort_option, expected_order):
    "Test sorting products by name"
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.sort_products(sort_option) # Selects "az" or "za"

    product_names = inventory_page.get_product_names()
    assert product_names == sorted(product_names, reverse=not expected_order), f"Sorting failed for {sort_option}"


@pytest.mark.parametrize("sort_option, expected_order",[
    ("lohi", True), # price low -> high
    ("hilo", False), # price high -> low
    ])
def test_sort_by_price(page: Page, sort_option, expected_order):
    "Test sorting products by price"
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.sort_products(sort_option) #Selects "lohi" or "hilo"

    product_prices = inventory_page.get_product_prices()
    assert product_prices == sorted(product_prices, reverse=not expected_order), f"Sorting failed for {sort_option}"

@pytest.mark.xfail(reason= "Cart is not cleared after logout — Cart should remember items for same user")
def test_cart_clears_after_logout(page: Page):
    login_page = LoginPage(page)
    login_page.goto_url()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart.click()     
    inventory_page.cart_button.click()  

    # Validate item is in cart
    expect(inventory_page.cart_badge).to_have_count(1)

    navigation_page = NavigationPage(page)
    navigation_page.logout()

    login_page.login("standard_user", "secret_sauce")

    inventory_page.cart_button.click()

    # Validate cart is empty, Should fail if same user logs back in
    expect(inventory_page.cart_badge).to_have_count(0)

from playwright.sync_api import Page
from pages.inventory_page import InventoryPage

class CheckoutPage:
    def __init__(self, page:Page, inventory_page: InventoryPage):
        self.page = page 
        self.inventory_page = inventory_page

        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")   
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.order_success_message = page.locator("[data-test=\"complete-header\"]")
        self.error_message = page.locator("[data-test='error']")
    
    def proceed_to_checkout(self):
        "Using inventory page cart button this time instead of defining again for a different approach"
        self.inventory_page.cart_button.click()
        self.checkout_button.click()

    def enter_shipping_details(self, first_name: str, last_name: str, postal_code: str):
        "Fill in the shipping details"
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def complete_checkout(self):
        "Complete checkout"
        self.finish_button.click()

    def get_error_text(self):
        return self.error_message.inner_text()
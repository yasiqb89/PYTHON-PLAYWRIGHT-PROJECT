from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator('.inventory_item')
        self.item_titles = page.locator('.inventory_item_name')
        self.cart_icon = page.locator('.shopping_cart_link')

        self.add_to_cart = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")
        self.remove_from_cart = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']") 

        self.add_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.add_bike_light = page.locator("[data-test='add-to-cart-sauce-labs-bike-light']")
        self.remove_backpack = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.remove_bike_light = page.locator("[data-test='remove-sauce-labs-bike-light']")
        self.item_prices = page.locator(".inventory_item_price") # Get common price locator using inspect element

        self.sort_dropdown = page.locator("[data-test=\"product-sort-container\"]")
        self.product_names = page.locator(".inventory_item_name")

        # simulating filtering by selecting a product (locators for method)
        self.first_product_name = page.locator(".inventory_item_name").first # First product
        self.first_product_price = page.locator(".inventory_item_price").first # First product price 
        self.first_product_desc = page.locator(".inventory_item_desc").first # First product description 

    def click_first_product(self):
        "Click first product on the page"
        self.first_product_name.click()

    def add_item_to_cart(self):
        "Adds product to cart"
        self.add_to_cart.click()

    def remove_item_from_cart(self):
        "Removes a product from cart"
        self.remove_from_cart.click()

    def open_cart(self):
        "Cart button to cart page"
        self.cart_button.click()

    def add_multiple_items_to_cart(self):
        "Add two products to cart"
        self.add_backpack.click()
        self.add_bike_light.click()
    
    def remove_item_from_cart(self):
        "Remove an item from cart"
        self.remove_backpack.click()

    def get_cart_total(self):
        "Calculate total price of items in cart" 
        prices = self.item_prices.all_inner_texts()
        total_price = sum(float(price.replace("$", "")) for price in prices)
        return total_price
    
    def sort_products(self, option: str):
        "selects a sorting option from the dropdown"
        self.sort_dropdown.select_option(option)

    def get_product_names(self):
        "Returns a list of all product names"
        return self.product_names.all_inner_texts()
    
    def get_product_prices(self):
        "Returns a list of product prices in float"
        prices = self.item_prices.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def get_product_count(self):
        return self.inventory_items.count()

    def get_all_product_names(self):
        return self.item_titles.count()
    
    def get_all_product_names(self):
        expect(self.item_titles.first).to_be_visible()
        return self.item_titles.all_inner_texts()
    
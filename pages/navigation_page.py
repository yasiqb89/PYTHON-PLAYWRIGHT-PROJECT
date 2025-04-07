from playwright.sync_api import Page
from pages import navigation_page

class NavigationPage:
    "Page object model for navigation"

    def __init__(self, page:Page):
        self.page = page
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.menu_close_button = page.get_by_role("button", name="Close Menu")
        self.all_items_link = page.locator("[data-test=\"inventory-sidebar-link\"]")
        self.about_link = page.locator("[data-test=\"about-sidebar-link\"]")
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")
        self.logout_link = page.locator("[data-test=\"logout-sidebar-link\"]")
        self.back_to_products_button = page.locator("[data-test='back-to-products']")

    def open_menu(self):
        "Opens sidebar menu"
        self.menu_button.click()

    def navigate_to_all_items(self):
        "clicks on All items link in the sidebar menu"
        self.open_menu()
        self.all_items_link.click()

    def navigate_to_about(self):
        "Click on About in sidebar menu"
        self.open_menu()
        self.about_link.click()  

    def navigate_to_cart(self):
        "Click on cart button on main page"
        self.cart_button.click()

    def logout(self):
        "Logs out user"
        self.open_menu()
        self.logout_link.click()
class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.go_to_cart = page.locator(".shopping_cart_container")
        self.add_to_cart = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )

    def add_backpack_to_cart(self):
        self.add_to_cart.click()

    def open_cart(self):
        self.go_to_cart.click()
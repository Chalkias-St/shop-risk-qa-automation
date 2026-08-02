class CartPage:

    def __init__(self, page):
        self.page = page

        self.cart_item_name = page.locator('[data-test="inventory-item-name"]')
        self.remove_backpack_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )
        self.checkout_button = page.locator("#checkout")

    def get_cart_item_name(self):
        return self.cart_item_name.text_content()

    def is_item_in_cart(self, expected_item):
        if self.cart_item_name.count() == 0:
            return False

        return expected_item in self.get_cart_item_name()

    def remove_backpack_from_cart(self):
        self.remove_backpack_button.click()

    def proceed_to_checkout(self):
        self.checkout_button.click()
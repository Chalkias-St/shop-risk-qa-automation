class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")

        self.continue_button = page.locator("#continue")
        self.cancel_button = page.locator("#cancel")
        self.finish_button = page.locator("#finish")

        self.success_message = page.locator(
            '[data-test="complete-header"]'
        )
        self.error_message = page.locator('[data-test="error"]')

    def fill_checkout_info(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def click_cancel(self):
        self.cancel_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_success_message(self):
        return self.success_message.text_content()

    def get_error_message(self):
        return self.error_message.text_content()

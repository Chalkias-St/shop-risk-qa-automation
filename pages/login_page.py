from config.settings import UI_BASE_URL
class LoginPage:

    def __init__(self, page):
        self.page = page
        #locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')    
    
    def navigate(self):
        self.page.goto(UI_BASE_URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def get_error_message(self):
        return self.error_message.text_content()

    def is_inventory_page_loaded(self):
         return self.page.locator(".inventory_list").is_visible()
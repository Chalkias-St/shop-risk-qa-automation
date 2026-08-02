import pytest

from pages import login_page
from pages import inventory_page
from pages import cart_page
from pages import checkout_page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.test_data import VALID_USERNAME, VALID_PASSWORD

@pytest.mark.ui
@pytest.mark.regression
def test_successful_checkout_flow(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert login_page.is_inventory_page_loaded()

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    assert cart_page.is_item_in_cart("Sauce Labs Backpack")
    cart_page.proceed_to_checkout()

    checkout_page.fill_checkout_info(
    "Stathis",
    "Chalkias",
    "12345"
    )   

    checkout_page.continue_checkout()
    checkout_page.finish_order()

    success_message = checkout_page.get_success_message()
    assert "Thank you for your order!" in success_message
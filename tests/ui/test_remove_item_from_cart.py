from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.test_data import VALID_USERNAME, VALID_PASSWORD
import pytest

@pytest.mark.ui
@pytest.mark.regression

def test_remove_item_from_cart(page):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert login_page.is_inventory_page_loaded()

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    assert cart_page.is_item_in_cart("Sauce Labs Backpack")

    cart_page.remove_backpack_from_cart()
    assert not cart_page.is_item_in_cart("Sauce Labs Backpack")
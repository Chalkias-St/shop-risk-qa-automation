import pytest

from data.test_data import VALID_PASSWORD, VALID_USERNAME
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.parametrize(
    "first_name,last_name,postal_code,expected_error",
    [
        ("", "", "", "Error: First Name is required"),
        ("Stathis", "", "", "Error: Last Name is required"),
        ("Stathis", "Chalkias", "", "Error: Postal Code is required"),
    ],
)
def test_checkout_required_field_validation(
    page,
    first_name,
    last_name,
    postal_code,
    expected_error,
):
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
    checkout_page.fill_checkout_info(first_name, last_name, postal_code)
    checkout_page.continue_checkout()

    assert checkout_page.get_error_message() == expected_error

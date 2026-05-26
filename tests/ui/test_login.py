from pages.login_page import LoginPage
from data.test_data import VALID_USERNAME, VALID_PASSWORD
import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert login_page.is_inventory_page_loaded() is True
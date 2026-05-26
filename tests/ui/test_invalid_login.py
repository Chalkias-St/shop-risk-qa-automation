from pages.login_page import LoginPage
from data.test_data import VALID_USERNAME, INVALID_PASSWORD
import pytest

@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_USERNAME, INVALID_PASSWORD)
    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message

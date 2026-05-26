import pytest

from pages.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.regression

@pytest.mark.parametrize(
    "username,password,expected_result",
    [
        ("standard_user", "secret_sauce", True),
        ("standard_user", "wrong_password", False),
    ]
)
def test_login(page, username, password, expected_result):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(username, password)

    if expected_result:

        assert login_page.is_inventory_page_loaded()

    else:

        error_message = login_page.get_error_message()

        assert "Username and password do not match" in error_message
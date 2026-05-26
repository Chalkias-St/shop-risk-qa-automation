import pytest
from config.settings import UI_BASE_URL

@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_login_page_is_loaded(page):
    page.goto(UI_BASE_URL)

    assert page.locator("#user-name").is_visible()
    assert page.locator("#password").is_visible()
    assert page.locator("#login-button").is_visible()
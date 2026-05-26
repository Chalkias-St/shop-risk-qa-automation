from api.users_api import UsersAPI
import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_create_user():
    users_api = UsersAPI()
    user_stathis = {
        "name": "Stathis",
        "job": "QA Engineer"
    }
    response = users_api.create_user(user_stathis)

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Stathis"
    assert body["job"] == "QA Engineer"
import json
from api.users_api import UsersAPI
import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_get_single_user():

    users_api = UsersAPI()
    response = users_api.get_user(1)

    body = response.json()

    print(json.dumps(body, indent=4))

    response_time = response.elapsed.total_seconds()

    print(f"\nResponse Time: {response_time}")

    assert response.status_code == 200

    assert response_time < 60

    assert body["id"] == 1
    assert body["name"] == "Leanne Graham"
    assert "@" in body["email"]
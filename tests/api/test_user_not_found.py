import requests
import pytest

@pytest.mark.api
@pytest.mark.regression
def test_user_not_found():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999"
    )
    body = response.json()
    status_code = response.status_code
    print(f"\nBody: {body}")
    print(f"\nStatus Code: {status_code}")


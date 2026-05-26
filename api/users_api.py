import requests
from config.settings import API_BASE_URL



class UsersAPI:

    def get_user(self, user_id):

        return requests.get(
            f"{API_BASE_URL}/users/{user_id}"
        )

    def create_user(self, user_data):

        return requests.post(
            f"{API_BASE_URL}/users",
            json=user_data
        )
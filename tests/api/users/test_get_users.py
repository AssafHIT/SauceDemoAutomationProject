import pytest
import requests
from utils.config import ConfigReader
from utils.helpers import validate_user_field

api_base_url = ConfigReader.read_config("settings", "api_base_url")  # Added api_base_url from config.ini

class TestUserAPI:
    @pytest.mark.critical
    def test_get_all_products(self):
        response = requests.get(f"{api_base_url}/users")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"
        json_response = response.json()
        assert isinstance(json_response, list), "Expected response JSON to be a list"

    @pytest.mark.parametrize("field", ['id', 'email', 'username'])
    def test_valid_user_fields(self, field):
        user = requests.get(f"{api_base_url}/users/1").json()
        assert field in user, f"User {user['id']} is missing '{field}' field"
        validate_user_field(user, field)

    @pytest.mark.parametrize("user_id", [1])  # Brackets for Passing id as Int
    def test_get_user_by_id(self, user_id):
        response = requests.get(f"{api_base_url}/users/{user_id}")
        json_response = response.json()
        assert json_response["id"] == user_id, f"Expected product id to be {user_id}, but got {json_response['id']}"
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"

    @pytest.mark.parametrize("user_id", [2])
    def test_get_single_user_existing_keys(self, user_id):

        response = requests.get(f"{api_base_url}/users/{user_id}")
        json_response = response.json()
        assert all(field in json_response for field in ['id', 'email', 'username']), "User is missing important information"

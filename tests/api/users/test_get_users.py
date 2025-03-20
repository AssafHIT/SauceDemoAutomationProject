import pytest
import requests
from utils.config import ConfigReader

api_base_url = ConfigReader.read_config("settings", "api_base_url")  # Added api_base_url from config.ini

class TestProductAPI:
    @pytest.mark.critical
    def test_get_all_products(self):
        response = requests.get(f"{api_base_url}/users")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"
        json_response = response.json()
        assert isinstance(json_response, list), "Expected response JSON to be a list"

    @pytest.mark.parametrize("user_id", [1])  # Brackets for Passing id as Int
    def test_get_user_by_id(self, user_id):
        response = requests.get(f"{api_base_url}/users/{user_id}")
        json_response = response.json()
        assert json_response[
                   "id"] == user_id, f"Expected user id to be {user_id}, but got {json_response['id']}"
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"


import pytest
import requests
from utils.config import ConfigReader
from utils.helpers import validate_product_field

api_base_url = ConfigReader.read_config("settings", "api_base_url")  # Added api_base_url from config.ini

class TestProductAPI:
    @pytest.mark.critical
    def test_get_all_products(self):
        response = requests.get(f"{api_base_url}/carts")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"
        json_response = response.json()
        assert isinstance(json_response, list), "Expected response JSON to be a list"


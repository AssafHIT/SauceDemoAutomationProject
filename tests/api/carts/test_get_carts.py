import pytest
import requests
from utils.config import ConfigReader
from utils.helpers import validate_product_field

api_base_url = ConfigReader.read_config("settings", "api_base_url")  # Added api_base_url from config.ini

class TestCartAPI:
    @pytest.mark.critical
    def test_get_all_carts(self):
        response = requests.get(f"{api_base_url}/carts")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"
        json_response = response.json()
        assert isinstance(json_response, list), "Expected response JSON to be a list"

    @pytest.mark.parametrize("field", ['id', 'userId', 'products'])  # Fields you want to validate
    def test_valid_cart_fields(self, field):
        carts = requests.get(f"{api_base_url}/carts").json()
        for cart in carts:
            # Check if the field exists in the cart
            assert field in cart, f"Cart {cart['id']} is missing '{field}' field"
            validate_product_field(cart, field)  # You may need to adjust the validation function for carts

    @pytest.mark.parametrize("cart_id", [2])  # Replace with appropriate cart ID
    def test_get_cart_by_id(self, cart_id):
        response = requests.get(f"{api_base_url}/carts/{cart_id}")
        json_response = response.json()
        assert json_response["id"] == cart_id, f"Expected cart id to be {cart_id}, but got {json_response['id']}"
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"

    @pytest.mark.parametrize("cart_id", [2])  # Replace with appropriate cart ID
    def test_get_single_cart_existing_keys(self, cart_id):
        response = requests.get(f"{api_base_url}/carts/{cart_id}")
        json_response = response.json()
        # Check that keys like 'id', 'userId', and 'products' exist in the response
        assert all(field in json_response for field in ['id', 'userId', 'products']), "Cart is missing important information"

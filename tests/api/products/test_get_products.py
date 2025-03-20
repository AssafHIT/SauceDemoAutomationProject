import pytest
import requests
from utils.config import ConfigReader
from utils.helpers import validate_product_field

api_base_url = ConfigReader.read_config("settings", "api_base_url")  # Added api_base_url from config.ini

class TestProductAPI:
    @pytest.mark.critical
    def test_get_all_products(self):
        response = requests.get(f"{api_base_url}/products")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"
        json_response = response.json()
        assert isinstance(json_response, list), "Expected response JSON to be a list"

    @pytest.mark.parametrize("field", ['id', 'title', 'price', 'description', 'category', 'image', 'rating'])
    def test_valid_product_fields(self, field):
        products = requests.get(f"{api_base_url}/products").json()
        for product in products:
            # Check if the field exists in the product
            assert field in product, f"Product {product['id']} is missing '{field}' field"
            validate_product_field(product, field)

    @pytest.mark.parametrize("product_id", [2])  # Brackets for Passing id as Int
    def test_get_product_by_id(self, product_id):
        response = requests.get(f"{api_base_url}/products/{product_id}")
        json_response = response.json()
        assert json_response["id"] == product_id, f"Expected product id to be {product_id}, but got {json_response['id']}"
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"

    @pytest.mark.parametrize("product_id", [2])  # Brackets for Passing id as Int
    def test_get_single_user_existing_keys(self, product_id):
        response = requests.get(f"{api_base_url}/products/{product_id}")
        json_response = response.json()
        assert 'title' in json_response.keys() and 'price' in json_response.keys(), "Product is missing title and price"

import pytest
import requests
from utils.config import ConfigReader
from utils.helpers import validate_product_field

api_base_url = ConfigReader.read_config("settings", "api_base_url")  # Added api_base_url from config.ini
## Helper function to validate each field:
#def validate_product_field(product, field):
#    if field == 'price':  # Price should be a positive (int) or (float)
#        assert isinstance(product['price'], (int, float)), f"Product price is not a valid number: {product['price']}"
#        assert product['price'] > 0, f"Product price is non-positive: {product['price']}"
#    elif field == 'rating':  # 'rate' and 'count' are keys in 'rating', and rate should be between 1 - 5
#        assert isinstance(product['rating'], dict), f"Product rating is not a dictionary: {product['rating']}"
#        assert 'rate' in product['rating'], "Product rating is missing 'rate' field"
#        assert 'count' in product['rating'], "Product rating is missing 'count' field"
#        assert 1 <= product['rating']['rate'] <= 5, f"Product rating is out of bounds: {product['rating']['rate']}"
#    elif field == 'id':  # ID should be a positive (int)
#        assert isinstance(product['id'], int) and product['id'] > 0, f"Product ID is invalid: {product['id']}"
#    elif field == 'category':  # Check for valid 'category'
#        assert isinstance(product['category'], str) and len(product['category']) > 0, f"Product category is invalid: {product['category']}"
#    elif field == 'title':  # Check for valid 'title'
#        assert isinstance(product['title'], str) and len(product['title']) > 0, f"Product title is invalid: {product['title']}"
#    elif field == 'description':  # Check for valid 'description'
#        assert isinstance(product['description'], str) and len(product['description']) > 0, f"Product description is invalid: {product['description']}"
#    elif field == 'image':  # Check for valid 'image'
#        assert isinstance(product['image'], str) and len(product['image']) > 0, f"Product image is invalid: {product['image']}"

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

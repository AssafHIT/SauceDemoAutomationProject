import pytest
import requests
from utils.config import ConfigReader

api_base_url = ConfigReader.read_config("settings", "api_base_url")  # Added api_base_url from config.ini

class TestCreateCart:
    @pytest.mark.critical
    def test_create_cart(self):
        cart_data = {
            "userId": 1,
            "products": [
                {
                    "productId": 1,
                    "quantity": 2
                },
                {
                    "productId": 3,
                    "quantity": 1
                }
            ]
        }

        response = requests.post(f"{api_base_url}/carts", json=cart_data)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        json_response = response.json()
        assert "id" in json_response, "Response does not contain 'id'"
        assert json_response["userId"] == cart_data[
            "userId"], f"Expected userId {cart_data['userId']}, but got {json_response['userId']}"
        assert "products" in json_response, "Response does not contain 'products'"

        for product in cart_data["products"]:
            assert any(prod["productId"] == product["productId"] and prod["quantity"] == product["quantity"] for prod in
                       json_response["products"]), \
                f"Product {product['productId']} with quantity {product['quantity']} is missing or incorrect in the response"
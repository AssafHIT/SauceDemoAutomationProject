import random
import time

import allure
import pytest
from utils.config import ConfigReader

@allure.suite("Cart Management Tests")
@pytest.mark.usefixtures("setup", "login_page", "products_page", "cart_page")
class TestCart:
    # Using data from config.ini:
    valid_username = ConfigReader.read_config("login", "username")
    valid_password = ConfigReader.read_config("login", "password")
    user_firstname = ConfigReader.read_config("user_info", "firstname")
    user_lastname = ConfigReader.read_config("user_info", "lastname")
    user_zip = ConfigReader.read_config("user_info", "zip")

    @pytest.mark.critical
    def test_01_view_cart(self, login_page, products_page, cart_page, setup):

        login_page.fill_info(self.valid_username, self.valid_password)

        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)

        product_name = products_page.get_single_product_name(product_index)
        products_page.go_to_shopping_cart()

        cart_product_titles = cart_page.get_products_titles()

        assert product_name in cart_product_titles, f"Product '{product_name}' not found in the cart!"

    @pytest.mark.parametrize("product_index", [1, 2, 3, 4, 5, 6])
    def test_02_remove_item_from_cart(self, login_page, products_page, cart_page, setup, product_index):
        login_page.fill_info(self.valid_username, self.valid_password)

        products_page.add_to_cart(product_index)

        products_page.go_to_shopping_cart()
        cart_page.remove_item_by_index(0)

        assert cart_page.is_cart_empty(), "The cart is not empty after removing the item."
        assert cart_page.get_cart_items() == [], "Cart count should be 0 after removing the item."

    @pytest.mark.parametrize("firstname, lastname, zip, expected_error", [
        ("", user_lastname, user_zip, "Error: First Name is required"),
        (user_firstname, "", user_zip, "Error: Last Name is required"),
        (user_firstname, user_lastname, "", "Error: Postal Code is required"),
    ])
    def test_03_invalid_checkout_info(self, login_page, products_page, cart_page, setup, firstname, lastname, zip,
                                      expected_error):
        login_page.fill_info(self.valid_username, self.valid_password)
        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        products_page.go_to_shopping_cart()
        cart_page.checkout()
        error_message = cart_page.fill_info(firstname=firstname, lastname=lastname, zip=zip)

        assert error_message == expected_error, f"Expected error message: '{expected_error}', but got: '{error_message}'"

    def test_04_successful_checkout(self, login_page, products_page, cart_page, setup):

        login_page.fill_info(self.valid_username, self.valid_password)
        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        products_page.go_to_shopping_cart()
        cart_page.checkout()
        cart_page.fill_info(firstname = self.user_firstname, lastname = self.user_lastname, zip = self.user_zip)
        cart_page.finish_click()

        assert cart_page.get_checkout_message() == "Thank you for your order!", "Failed purchase!"
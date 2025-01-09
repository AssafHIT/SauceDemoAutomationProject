import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pages import item_page
from pages.cart_page import CartPage
from pages.item_page import ItemPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestCart:
    @allure.title("View Cart Test")
    @allure.description("This test verifies that a randomly added product appears in the shopping cart.")
    def test_01_view_cart(self):
        login_page = LoginPage(self.driver)
        cart_page = CartPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)

        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)

        product_name = products_page.get_single_product_name(product_index)
        products_page.go_to_shopping_cart()
        cart_product_titles = cart_page.get_products_titles()

        assert product_name in cart_product_titles, f"Product '{product_name}' not found in the cart!"

    @allure.title("Remove Item from Cart Test")
    @allure.description("This test verifies that an item can be added to the cart and then successfully removed, ensuring the cart is empty afterwards.")
    def test_02_remove_item_from_cart(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)


        products_page.add_to_cart(1)  # Assuming this function returns the first product element

        cart_page = CartPage(self.driver)
        products_page.go_to_shopping_cart()  # Assuming `go_to_cart()` method will navigate to the cart page
        cart_page.remove_item_by_index(0)  # Assuming this method removes the item from the cart
        assert cart_page.is_cart_empty(), "The cart is not empty after removing the item."
        assert cart_page.get_cart_items() == [], "Cart count should be 0 after removing the item."

    @allure.title("Missing First Name Test")
    @allure.description("This test validates that the checkout process does not proceed when the first name field is left blank during the information submission step.")
    def test_03_no_firstname(self):
        login_page = LoginPage(self.driver)
        cart_page = CartPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)
        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        products_page.go_to_shopping_cart()
        cart_page.checkout()
        cart_page.fill_info(firstname="", lastname="Yehezkel", zip="12345")

        assert cart_page.get_info_error_message() == "Error: First Name is required", "Purchase shouldn't continue!"

    @allure.title("Missing Last Name Test")
    @allure.description("This test validates that the checkout process does not proceed when the last name field is left blank during the information submission step.")
    def test_04_no_lastname(self):
        login_page = LoginPage(self.driver)
        cart_page = CartPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)
        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        products_page.go_to_shopping_cart()
        cart_page.checkout()
        cart_page.fill_info(firstname="Assaf", lastname="", zip="12345")

        assert cart_page.get_info_error_message() == "Error: Last Name is required", "Purchase shouldn't continue!"

    @allure.title("Missing Postal Code Test")
    @allure.description("This test validates that the checkout process does not proceed when the postal code field is left blank during the information submission step.")
    def test_05_no_postal_code(self):
        login_page = LoginPage(self.driver)
        cart_page = CartPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)
        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        products_page.go_to_shopping_cart()
        cart_page.checkout()
        cart_page.fill_info(firstname="Assaf", lastname="Yehezkel", zip="")

        assert cart_page.get_info_error_message() == "Error: Postal Code is required", "Purchase shouldn't continue!"

    @allure.title("Successful Checkout Test")
    @allure.description("This test verifies the successful completion of the checkout process, including filling in the checkout information and confirming the success message.")
    def test_06_successful_checkout(self):
        login_page = LoginPage(self.driver)
        cart_page = CartPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)
        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        products_page.go_to_shopping_cart()
        cart_page.checkout()
        cart_page.fill_info(firstname="Assaf", lastname="Yehezkel", zip="12345")

        assert cart_page.get_checkout_message() == "Thank you for your order!", "Failed purchase!"
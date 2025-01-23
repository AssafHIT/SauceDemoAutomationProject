import random

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.fixture(scope="function")
def driver():
    """Fixture to set up and tear down WebDriver."""
    options = Options()
    options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def products_page(driver):
    return ProductsPage(driver)


@pytest.fixture(scope="function")
def cart_page(driver):
    return CartPage(driver)

@allure.suite("Cart Management Tests")
@pytest.mark.usefixtures("driver", "login_page", "products_page", "cart_page")
class TestCart:
    base_url = "https://www.saucedemo.com"

    @pytest.mark.critical
    def test_01_view_cart(self, login_page, products_page, cart_page, driver):
        driver.get(self.base_url)
        login_page.fill_info("standard_user", "secret_sauce")

        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)

        product_name = products_page.get_single_product_name(product_index)
        products_page.go_to_shopping_cart()

        cart_product_titles = cart_page.get_products_titles()

        assert product_name in cart_product_titles, f"Product '{product_name}' not found in the cart!"

    @pytest.mark.parametrize("product_index", [1, 2, 3, 4, 5, 6])
    def test_02_remove_item_from_cart(self, login_page, products_page, cart_page, driver, product_index):
        driver.get(self.base_url)
        login_page.fill_info("standard_user", "secret_sauce")

        products_page.add_to_cart(product_index)

        products_page.go_to_shopping_cart()
        cart_page.remove_item_by_index(0)

        assert cart_page.is_cart_empty(), "The cart is not empty after removing the item."
        assert cart_page.get_cart_items() == [], "Cart count should be 0 after removing the item."

    @pytest.mark.parametrize("firstname, lastname, zip, expected_error", [
        ("", "Yehezkel", "12345", "Error: First Name is required"),
        ("Assaf", "", "12345", "Error: Last Name is required"),
        ("Assaf", "Yehezkel", "", "Error: Postal Code is required"),
    ])
    def test_03_invalid_checkout_info(self, login_page, products_page, cart_page, driver, firstname, lastname, zip,
                                      expected_error):
        driver.get(self.base_url)
        login_page.fill_info("standard_user", "secret_sauce")

        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        products_page.go_to_shopping_cart()
        cart_page.checkout()

        cart_page.fill_info(firstname=firstname, lastname=lastname, zip=zip)

        assert cart_page.get_info_error_message() == expected_error, "Purchase shouldn't continue!"

    def test_04_successful_checkout(self, login_page, products_page, cart_page, driver):
        driver.get(self.base_url)
        login_page.fill_info("standard_user", "secret_sauce")

        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        products_page.go_to_shopping_cart()
        cart_page.checkout()

        cart_page.fill_info(firstname="Assaf", lastname="Yehezkel", zip="12345")

        assert cart_page.get_checkout_message() == "Thank you for your order!", "Failed purchase!"
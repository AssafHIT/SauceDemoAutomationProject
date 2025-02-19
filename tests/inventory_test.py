import random
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

@allure.suite("Inventory Management Tests")
class TestInventory:

    @pytest.mark.critical
    @pytest.mark.parametrize(
        "item_count, description",
        [
            (1, "Add a Single Item to Cart"),
            (3, "Add Multiple Items to Cart"),
        ],
    )
    @allure.title("{description}")
    @allure.description("This test validates adding items to the cart updates the cart count correctly.")
    def test_01_add_items_to_cart(self, setup, item_count, description, login_page, products_page):
        login_page.fill_info("standard_user", "secret_sauce")

        available_products = list(range(1, 7))
        for _ in range(item_count):
            product_index = random.choice(available_products)
            available_products.remove(product_index)
            products_page.add_to_cart(product_index)

        cart_count = products_page.get_cart_count()
        assert cart_count == item_count, f"Expected {item_count} items in cart, but got {cart_count}."

    @pytest.mark.high
    @allure.title("Remove Item from Cart Test")
    @allure.description("This test validates removing an item from the cart decreases the cart count correctly.")
    def test_02_remove_item_from_cart(self, setup, login_page, products_page):
        login_page.fill_info("standard_user", "secret_sauce")

        product_index = random.randint(1, 6)
        products_page.add_to_cart(product_index)
        initial_cart_count = products_page.get_cart_count()
        assert initial_cart_count > 0, "Cart count did not increase after adding a product!"

        products_page.remove_from_cart(product_index)

        try:
            WebDriverWait(setup, 10).until(
                lambda setup: not products_page.is_cart_item_present(product_index)
            )
            updated_cart_count = 0
        except TimeoutException:
            updated_cart_count = products_page.get_cart_count()

        assert updated_cart_count == initial_cart_count - 1, (
            f"Expected cart count to decrease to {initial_cart_count - 1}, "
            f"but got {updated_cart_count}."
        )

    @pytest.mark.medium
    @allure.title("Validate Product Details Test")
    @allure.description("This test opens a product details page and validates the correct product details are displayed.")
    def test_03_validate_product_details(self, setup, login_page, products_page, item_page):
        login_page.fill_info("standard_user", "secret_sauce")

        product_index = random.randint(1, 6)
        expected_product_name = products_page.get_single_product_name(product_index)
        products_page.choose_product(product_index)
        actual_product_name = item_page.get_product_title()

        assert actual_product_name == expected_product_name, (
            f"Expected product name to be '{expected_product_name}', but got '{actual_product_name}'."
        )

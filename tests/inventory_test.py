import random
import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pages.item_page import ItemPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestInventory:
    @allure.title("Add Single Item to Cart Test")
    @allure.description("This test validates that adding a single random item to the cart results in the cart count being updated to 1.")
    def test_01_add_single_item_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        product_page = ProductsPage(self.driver)
        product_page.add_to_cart(random.randint(1, 6))
        cart_count = product_page.get_cart_count()
        assert cart_count == 1, f"Expected 1 items in cart, but got {cart_count}"

    @allure.title("Add Multiple Items to Cart Test")
    @allure.description("This test validates that adding multiple random items to the cart results in the correct cart count of 3 items.")
    def test_02_add_multiple_items(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        product_page = ProductsPage(self.driver)

        available_products = [1, 2, 3, 4, 5, 6]
        for _ in range(3):
            product_index = random.choice(available_products)
            available_products.remove(product_index)
            product_page.add_to_cart(product_index)

        cart_count = product_page.get_cart_count()
        assert cart_count == 3, f"Expected 3 items in cart, but got {cart_count}"

    @allure.title("Remove Item from Cart Test")
    @allure.description("This test validates that an item can be successfully removed from the cart and the cart count decreases accordingly.")
    def test_03_remove_item_from_cart(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        product_page = ProductsPage(self.driver)
        product_index = random.randint(1, 6)
        product_page.add_to_cart(product_index)
        cart_count = product_page.get_cart_count()
        assert cart_count > 0, "Cart count did not increase after adding a product!"

        product_page.remove_from_cart(product_index)

        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_elements(*ProductsPage.CART_COUNT) == []
            )
            # If the cart badge disappears ( = 0)
            updated_cart_count = 0
        except TimeoutException:

            updated_cart_count = product_page.get_cart_count()

        assert updated_cart_count == cart_count - 1, f"Expected cart count to decrease to {cart_count - 1}, "f"but got {updated_cart_count}."

    @allure.title("Validate Item Details Test")
    @allure.description("This test opens a product details page and validates that the correct product details are shown.")
    def test_04_valid_item_details(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        product_page = ProductsPage(self.driver)
        item_page = ItemPage(self.driver)

        product_index = random.randint(1, 6)
        product_name = product_page.get_single_product_name(product_index)
        product_page.choose_product(product_index)
        assert item_page.get_product_title() == product_name, "Wrong product!"

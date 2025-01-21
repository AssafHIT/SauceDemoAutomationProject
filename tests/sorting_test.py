import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestSort:

    @allure.title("Validate Price Sorting Functionality (Low to High)")
    @allure.description("This test sorts the products by price (low to high) and verifies the sorting order.")
    def test_01_price_sort_functionality_ascending(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        product_page = ProductsPage(self.driver)
        product_page.choose_sorting(2)
        product_prices = product_page.get_product_prices()
        assert product_prices == sorted(product_prices), "The products are not sorted by price (low to high)"

    @allure.title("Validate Price Sorting Functionality (High to Low)")
    @allure.description("This test sorts the products by price (high to low) and verifies the sorting order.")
    def test_02_price_sort_functionality_descending(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        product_page = ProductsPage(self.driver)
        product_page.choose_sorting(3)
        product_prices = product_page.get_product_prices()
        assert product_prices == sorted(product_prices, reverse=True), "The products are not sorted by price (high to low)"

    @allure.title("Validate Name Sorting Functionality (Z to A)")
    @allure.description("This test sorts the products by name (Z to A) and verifies the sorting order.")
    def test_03_name_sort_functionality_descending(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        product_page = ProductsPage(self.driver)
        product_page.choose_sorting(1)
        product_names = [name.text for name in product_page.get_product_names()]
        assert product_names == sorted(product_names, reverse=True), "The products are not sorted by name (Z to A)"

    @allure.title("Validate Name Sorting Functionality (A to Z)")
    @allure.description("This test sorts the products by name (A to Z) and verifies the sorting order.")
    def test_04_name_sort_functionality_ascending(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        product_page = ProductsPage(self.driver)
        product_page.choose_sorting(0)
        product_names = [name.text for name in product_page.get_product_names()]
        assert product_names == sorted(product_names), "The products are not sorted by name (A to Z)"










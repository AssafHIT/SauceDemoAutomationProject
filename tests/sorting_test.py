import pytest
import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Fixture to set up and tear down WebDriver."""
    options = Options()
    options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver  # Provide the WebDriver instance to the test

    driver.quit()  # Close browser after test

@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope="function")
def products_page(driver):
    return ProductsPage(driver)

@allure.suite("Sort Functionality Tests")
class TestSort:

    base_url = "https://www.saucedemo.com"

    @pytest.mark.critical
    @pytest.mark.parametrize(
        "sorting_option, is_descending, attribute, description",
        [
            (2, False, "price", "Price Sorting (Low to High)"),
            (3, True, "price", "Price Sorting (High to Low)"),
            (1, True, "name", "Name Sorting (Z to A)"),
            (0, False, "name", "Name Sorting (A to Z)"),
        ],
    )
    @allure.title("{description}")
    @allure.description("This test validates product sorting by {attribute}.")
    def test_01_sort_functionality(self, driver, sorting_option, is_descending, attribute, description, login_page, products_page):
        """
        Generalized test for validating sorting functionality.

        :param driver: WebDriver instance
        :param sorting_option: Sorting dropdown option index
        :param is_descending: Whether sorting is expected to be descending
        :param attribute: Attribute to validate (price or name)
        :param description: Test description for Allure report
        """
        driver.get(self.base_url)
        login_page.fill_info("standard_user", "secret_sauce")
        products_page.choose_sorting(sorting_option)

        # Validate sorting
        if attribute == "price":
            product_values = products_page.get_product_prices()
        elif attribute == "name":
            product_values = [name.text for name in products_page.get_product_names()]
        else:
            raise ValueError("Invalid attribute specified for sorting validation.")

        expected_values = sorted(product_values, reverse=is_descending)
        assert product_values == expected_values, (
            f"The products are not sorted by {attribute} "
            f"({'descending' if is_descending else 'ascending'} order)."
        )

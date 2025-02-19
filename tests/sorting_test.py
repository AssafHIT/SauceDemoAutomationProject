import pytest
import allure
from utils.config import ConfigReader

@allure.suite("Sort Functionality Tests")
class TestSort:
    # Using data from config.ini:
    valid_username = ConfigReader.read_config("login", "username")
    valid_password = ConfigReader.read_config("login", "password")
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
    def test_01_sort_functionality(self, setup, sorting_option, is_descending, attribute, description, login_page, products_page):
        login_page.fill_info(self.valid_username, self.valid_password)
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

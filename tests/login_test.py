import allure
import pytest

@allure.suite("Login Tests")
class TestLogin:

    base_url = "https://www.saucedemo.com"  # Base URL for the tests

    @pytest.mark.critical
    @pytest.mark.parametrize(
        "username, password, expected_url, expected_error_message, description",
        [
            ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", None,
             "Valid Login Test for Standard User"),
            ("standad_usr", "secret_sauce", None,
             "Epic sadface: Username and password do not match any user in this service",
             "Invalid Username Login Test"),
            ("standard_user", "secrt_suce", None,
             "Epic sadface: Username and password do not match any user in this service",
             "Invalid Password Login Test"),
            ("locked_out_user", "secret_sauce", None, "Epic sadface: Sorry, this user has been locked out.",
             "Locked-Out User Login Test"),
            ("", "secret_sauce", None, "Epic sadface: Username is required", "Login Without Username Test"),
            ("standard_user", "", None, "Epic sadface: Password is required", "Login Without Password Test"),
        ],
    )
    @allure.title("{description}")
    def test_01_login(self, driver, username, password, expected_url, expected_error_message, description, login_page):
        """Data-driven test for login functionality."""
        driver.get(self.base_url)  # Navigate to the base URL
        login_page.fill_info(username, password)

        if expected_url:
            # Valid login case
            assert driver.current_url == expected_url, f"Expected {expected_url}, but got {driver.current_url}."
        else:
            # Invalid login case
            error_message = login_page.get_error_message()
            assert error_message == expected_error_message, f"Expected error message: '{expected_error_message}', but got '{error_message}'."



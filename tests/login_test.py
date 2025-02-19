import allure
import pytest
from utils.config import ConfigReader

@allure.suite("Login Tests")
class TestLogin:
    # Using data from config.ini:
    valid_username = ConfigReader.read_config("login", "username")
    valid_password = ConfigReader.read_config("login", "password")
    base_url = ConfigReader.read_config("settings", "base_url")  # Added base_url from config.ini

    @pytest.mark.critical
    @pytest.mark.parametrize(
        "username, password, expected_url, expected_error_message, description",
        [
            (valid_username, valid_password, f"{base_url}/inventory.html", None,
             "Valid Login Test for Standard User"),
            ("standad_usr", valid_password, None,
             "Epic sadface: Username and password do not match any user in this service",
             "Invalid Username Login Test"),
            (valid_username, "secrt_suce", None,
             "Epic sadface: Username and password do not match any user in this service",
             "Invalid Password Login Test"),
            ("locked_out_user", valid_password, None, "Epic sadface: Sorry, this user has been locked out.",
             "Locked-Out User Login Test"),
            ("", valid_password, None, "Epic sadface: Username is required", "Login Without Username Test"),
            (valid_username, "", None, "Epic sadface: Password is required", "Login Without Password Test"),
        ],
    )
    @allure.title("{description}")
    def test_01_login(self, setup, username, password, expected_url, expected_error_message, description, login_page):
        login_page.fill_info(username, password)

        if expected_url:
            # Valid login case
            assert setup.current_url == expected_url, f"Expected {expected_url}, but got {setup.current_url}."
        else:
            # Invalid login case
            error_message = login_page.get_error_message()
            assert error_message == expected_error_message, f"Expected error message: '{expected_error_message}', but got '{error_message}'."

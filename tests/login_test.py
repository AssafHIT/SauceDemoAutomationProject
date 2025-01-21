import allure
import pytest
from pages.login_page import LoginPage
from selenium import webdriver

class TestLogin:
    @allure.suite("Login Tests")
    class TestLogin:

        def setUp(self):
            self.driver = webdriver.Chrome()  # Start fresh browser instance for each test
            self.base_url = "https://www.saucedemo.com"  # Base URL for the tests
            self.driver.get(self.base_url)  # Open the base URL before each test

        def tearDown(self):
            try:
                print("Closing browser")
                self.driver.close()  # Close the current window
                self.driver.quit()  # Quit the entire browser session
            except Exception as e:
                print(f"Error in tearDown: {e}")

        #@pytest.mark.critical
        #@pytest.mark.parametrize(
        #    "username, password, expected_url, expected_error_message, description",
        #    [
        #        ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", None,
        #         "Valid Login Test for Standard User"),
        #        ("standad_usr", "secret_sauce", None,
        #         "Epic sadface: Username and password do not match any user in this service",
        #         "Invalid Username Login Test"),
        #        ("standard_user", "secrt_suce", None,
        #         "Epic sadface: Username and password do not match any user in this service",
        #         "Invalid Password Login Test"),
        #        ("locked_out_user", "secret_sauce", None, "Epic sadface: Sorry, this user has been locked out.",
        #         "Locked-Out User Login Test"),
        #        ("", "secret_sauce", None, "Epic sadface: Username is required", "Login Without Username Test"),
        #        ("standard_user", "", None, "Epic sadface: Password is required", "Login Without Password Test"),
        #    ],
        #)
        #@allure.title("{description}")
        #def test_login(self, username, password, expected_url, expected_error_message, description):
        #    """Data-driven test for login functionality."""
        #    login_page = LoginPage(self.driver)
        #    login_page.fill_info(username, password)
#
        #    if expected_url:
        #        # Valid login case
        #        assert self.driver.current_url == expected_url, f"Expected {expected_url}, but got {self.driver.current_url}."
        #    else:
        #        # Invalid login case
        #        error_message = login_page.get_error_message()
        #        assert error_message == expected_error_message, f"Expected error message: '{expected_error_message}', but got '{error_message}'."
#
        #    # Returning to base URL after each test
        #    print("Returning to base URL")
        #    self.driver.get(self.base_url)
    @pytest.mark.critical
    @allure.title("Valid Login Test for Standard User")
    @allure.description("This test verifies that the 'standard_user' can successfully log in and be redirected to the inventory page.")
    def test_01_valid_login_standard_user(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secret_sauce")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Failed to login."

    @pytest.mark.critical
    @allure.title("Invalid Username Login Test")
    @allure.description("This test verifies that attempting to log in with an incorrect username ('standad_usr') displays the correct error message and prevents login.")
    def test_02_invalid_username_standard_user(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standad_usr", "secret_sauce")
        error_message = login_page.get_error_message()
        assert error_message, "Login was successful!"

    @pytest.mark.critical
    @allure.title("Invalid Password Login Test")
    @allure.description("This test verifies that attempting to log in with an incorrect password ('secrt_suce') displays the correct error message and prevents login.")
    def test_03_invalid_password_standard_user(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "secrt_suce")
        error_message = login_page.get_error_message()
        assert error_message == "Epic sadface: Username and password do not match any user in this service", "Login was successful!"



    @pytest.mark.critical
    @allure.title("Locked-Out User Login Test")
    @allure.description("This test verifies that attempting to log in with the locked-out user credentials ('locked_out_user') displays the correct error message and prevents login.")
    def test_04_login_locked_out_user(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("locked_out_user", "secret_sauce")
        error_message = login_page.get_error_message()
        print(error_message)
        assert error_message == "Epic sadface: Sorry, this user has been locked out.", "Login was successful!"

    @pytest.mark.critical
    @allure.title("Login Without Username Test")
    @allure.description("This test verifies that attempting to log in without providing a username displays the correct error message and prevents login.")
    def test_05_no_username_login(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("", "secret_sauce")
        error_message = login_page.get_error_message()
        print(error_message)
        assert error_message == "Epic sadface: Username is required", "Login was successful!"

    @pytest.mark.critical
    @allure.title("Login Without Password Test")
    @allure.description("This test verifies that attempting to log in without providing a password displays the correct error message and prevents login.")
    def test_06_no_password_login(self):
        login_page = LoginPage(self.driver)
        login_page.fill_info("standard_user", "")
        error_message = login_page.get_error_message()
        print(error_message)
        assert error_message == "Epic sadface: Password is required", "Login was successful!"




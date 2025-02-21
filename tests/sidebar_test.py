import random
import time
import pytest
import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import ConfigReader


class TestSidebar:
    # Using data from config.ini:
    valid_username = ConfigReader.read_config("login", "username")
    valid_password = ConfigReader.read_config("login", "password")
    base_url = ConfigReader.read_config("settings", "base_url")

    @allure.title("Validate Sidebar Functionality")
    @allure.description("This test validates sidebar functionality.")
    def test_01_sidebar_functionality(self, setup, login_page, sidebar_page):
        login_page.fill_info(self.valid_username, self.valid_password)
        sidebar_page.open_sidebar()

        sidebar_page.wait_for_element_visible(sidebar_page._CLOSE_SIDE_MENU) # Wait for the sidebar to appear
        sidebar_visible = sidebar_page.is_element_displayed(sidebar_page._CLOSE_SIDE_MENU) # Verify if the sidebar is visible
        assert sidebar_visible, "Sidebar is not visible after opening."

        sidebar_page.click(sidebar_page._CLOSE_SIDE_MENU)
        sidebar_closed = sidebar_page.is_element_displayed(sidebar_page._SIDE_MENU_BTN)
        assert sidebar_closed, "Sidebar is not closed after clicking the close button."

    @allure.title("Validate About Button")
    @allure.description("This test validates the About button functionality.")
    def test_02_about_page_navigation(self, setup, login_page, sidebar_page):
        login_page.fill_info(self.valid_username, self.valid_password)
        sidebar_page.go_to_about_page()

        current_url = sidebar_page.driver.current_url.rstrip('/')
        expected_url = "https://saucelabs.com"
        assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"

    @allure.title("Validate Reset Button")
    @allure.description("This test validates the app reset functionality.")
    def test_03_app_reset_functionality(self, setup, login_page, sidebar_page, products_page, cart_page):
        login_page.fill_info(self.valid_username, self.valid_password)
        products_page.add_to_cart(random.randint(1, 6))

        WebDriverWait(sidebar_page.driver, 10).until(
            EC.text_to_be_present_in_element(products_page._CART_COUNT,"1"))

        cart_badge = sidebar_page.driver.find_element(*products_page._CART_COUNT)
        assert int(cart_badge.text) > 0, f"Cart is empty, expected at least 1 item, but found {cart_badge.text}."

        sidebar_page.reset_app_state()
        time.sleep(1)

        # Wait for the cart badge to disappear or be empty
        WebDriverWait(sidebar_page.driver, 10).until(
            EC.invisibility_of_element_located(products_page._CART_COUNT))


        try:
            cart_badge_after_reset = sidebar_page.driver.find_element(*products_page._CART_COUNT)
            assert cart_badge_after_reset.text == "", f"Expected empty cart, but found {cart_badge_after_reset.text}."
        except NoSuchElementException:
            # If the element is not found, the cart is empty, which is fine
            pass

    @allure.title("Validate Login Out Successfully")
    @allure.description("This test validates the logging out functionality.")
    def test_04_logout(self, setup, login_page, sidebar_page, products_page, cart_page):
        login_page.fill_info(self.valid_username, self.valid_password)
        current_url = sidebar_page.driver.current_url.rstrip('/')
        assert current_url == f"{self.base_url}/inventory.html", "Did not log in successfully."
        sidebar_page.logout()
        time.sleep(1)
        current_url = sidebar_page.driver.current_url.rstrip('/')
        assert current_url != f"{self.base_url}/inventory.html", "Failed to log out; still on inventory page."

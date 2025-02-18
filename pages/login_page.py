from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPage(BasePage):

    _USER_NAME = (By.CSS_SELECTOR, "#user-name")
    _PASSWORD = (By.CSS_SELECTOR, "#password")
    _LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    _ERROR_MSG = (By.CSS_SELECTOR, ".login-box h3")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_info(self, username, password):
        self.fill_text(self._USER_NAME, username)  # Use BasePage's fill_text
        self.fill_text(self._PASSWORD, password)  # Use BasePage's fill_text
        self.click(self._LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(self._ERROR_MSG)
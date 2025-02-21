import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage

class SideBarPage(BasePage):
    _SIDE_MENU_BTN = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    _CLOSE_SIDE_MENU = (By.CSS_SELECTOR, "#react-burger-cross-btn")
    _ABOUT_BTN = (By.CSS_SELECTOR, "#about_sidebar_link")
    _RESET_APP_STATE_BTN = (By.CSS_SELECTOR, "#reset_sidebar_link")
    _LOGOUT_BTN = (By.CSS_SELECTOR, "#logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def open_sidebar(self):
        self.click(self._SIDE_MENU_BTN)

    def go_to_about_page(self):
        self.click(self._SIDE_MENU_BTN)
        self.click(self._ABOUT_BTN)

    def reset_app_state(self):
        self.click(self._SIDE_MENU_BTN)
        self.click(self._RESET_APP_STATE_BTN)

    def logout(self):
        self.click(self._SIDE_MENU_BTN)
        self.click(self._LOGOUT_BTN)
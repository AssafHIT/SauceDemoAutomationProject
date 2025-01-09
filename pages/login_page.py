import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage

class LoginPage(BasePage):

    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    ERROR_MSG = (By.CSS_SELECTOR, ".login-box h3")


    def __init__(self, driver):
        self.driver: WebDriver = driver

    def fill_info(self, username, password):
        self.fill_text(self.USER_NAME, username)  # Use BasePage's fill_text
        self.fill_text(self.PASSWORD, password)  # Use BasePage's fill_text
        self.click(self.LOGIN_BTN)
        #self.driver.find_element(*self.USER_NAME).send_keys(username)
        #self.driver.find_element(*self.PASSWORD).send_keys(password)
        #self.driver.find_element(*self.LOGIN_BTN).click()



    def get_error_message(self):
        #error_message = self.driver.find_element(*self.ERROR_MSG).text
        #return error_message
        return self.get_text(self.ERROR_MSG)
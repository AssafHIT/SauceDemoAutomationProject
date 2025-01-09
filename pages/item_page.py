import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class ItemPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart")
    BACK = (By.CSS_SELECTOR, "#back-to-products")
    TITLE = (By.CSS_SELECTOR, ".inventory_details_name")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def add_product(self):
        #self.driver.find_element(*self.ADD_TO_CART).click()
        self.click(self.ADD_TO_CART)


    def back_to_products(self):
        #self.driver.find_element(*self.BACK).click()
        self.click(self.BACK)

    def get_product_title(self):
        #title = self.driver.find_element(*self.TITLE).text
        title =  self.get_text(self.TITLE)
        return title

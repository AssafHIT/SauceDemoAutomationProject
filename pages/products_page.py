import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.BasePage import BasePage

class ProductsPage(BasePage):

    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    SORT_SELECT = (By.CSS_SELECTOR, ".product_sort_container")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    CART_COUNT = (By.CSS_SELECTOR, ".shopping_cart_badge")


    def __init__(self, driver):
        self.driver: WebDriver = driver

    def choose_product(self, index):
        product_selector = (By.CSS_SELECTOR, f".inventory_item:nth-of-type({index}) .inventory_item_name")
        #self.driver.find_element(*product_selector).click()
        self.click(product_selector)
        time.sleep(1)

    def add_to_cart(self, index):
        add_to_cart_selector = (By.CSS_SELECTOR, f".inventory_item:nth-of-type({index}) .btn.btn_primary.btn_small.btn_inventory")
        #self.driver.find_element(*add_to_cart_selector).click()
        self.click(add_to_cart_selector)

    def remove_from_cart(self, index):
        remove_from_cart_selector = (By.CSS_SELECTOR, f".inventory_item:nth-of-type({index}) .btn.btn_secondary.btn_small.btn_inventory ")
        #self.driver.find_element(*remove_from_cart_selector).click()
        self.click(remove_from_cart_selector)


    def go_to_shopping_cart(self):
        #self.driver.find_element(*self.SHOPPING_CART).click()
        self.click(self.SHOPPING_CART)

    def choose_sorting(self, index):
        dropdown = self.driver.find_element(*self.SORT_SELECT)
        select = Select(dropdown)
        select.select_by_index(index)

    def get_product_prices(self):
        prices = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(price.text.replace('$', '').strip()) for price in prices]

    def get_product_names(self):
        names = self.driver.find_elements(*self.PRODUCT_NAME)
        return names

    def get_cart_count(self):
        count = int(self.driver.find_element(*self.CART_COUNT).text)
        return int(count)

    def get_single_product_name(self, index):
        product_selector = (By.CSS_SELECTOR, f".inventory_item:nth-of-type({index}) .inventory_item_name")
        return self.get_text(product_selector)
        #return self.driver.find_element(*product_selector).text

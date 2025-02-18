import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage

class ProductsPage(BasePage):

    _PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    _SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    _SORT_SELECT = (By.CSS_SELECTOR, ".product_sort_container")
    _PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    _CART_COUNT = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_product(self, index):
        product_selector = (By.CSS_SELECTOR, f".inventory_item:nth-of-type({index}) .inventory_item_name")
        self.click(product_selector)
        time.sleep(1)

    def add_to_cart(self, index):
        add_to_cart_selector = (By.CSS_SELECTOR, f".inventory_item:nth-of-type({index}) .btn.btn_primary.btn_small.btn_inventory")
        self.click(add_to_cart_selector)

    def remove_from_cart(self, index):
        remove_from_cart_selector = (By.CSS_SELECTOR, f".inventory_item:nth-of-type({index}) .btn.btn_secondary.btn_small.btn_inventory ")
        self.click(remove_from_cart_selector)


    def go_to_shopping_cart(self):
        self.click(self._SHOPPING_CART)

    def choose_sorting(self, index):
        dropdown = self.driver.find_element(*self._SORT_SELECT)
        select = Select(dropdown)
        select.select_by_index(index)

    def get_product_prices(self):
        prices = self.driver.find_elements(*self._PRODUCT_PRICES)
        return [float(price.text.replace('$', '').strip()) for price in prices]

    def get_product_names(self):
        names = self.driver.find_elements(*self._PRODUCT_NAME)
        return names

    def get_cart_count(self):
        count = int(self.driver.find_element(*self._CART_COUNT).text)
        return int(count)

    def get_single_product_name(self, index):
        product_selector = (By.CSS_SELECTOR, f".inventory_item:nth-of-type({index}) .inventory_item_name")
        return self.get_text(product_selector)

    def is_cart_item_present(self, product_index):
        try:

            cart_item_locator = (By.CSS_SELECTOR, f"#cart_item_{product_index}")
            self.driver.find_element(*cart_item_locator)
            return True
        except NoSuchElementException:
            return False

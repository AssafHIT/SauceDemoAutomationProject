from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class ItemPage(BasePage):

    _ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart")
    _BACK = (By.CSS_SELECTOR, "#back-to-products")
    _TITLE = (By.CSS_SELECTOR, ".inventory_details_name")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product(self):
        self.click(self._ADD_TO_CART)

    def back_to_products(self):
        self.click(self._BACK)

    def get_product_title(self):
        title =  self.get_text(self._TITLE)
        return title

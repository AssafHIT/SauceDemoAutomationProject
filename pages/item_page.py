from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class ItemPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart")
    BACK = (By.CSS_SELECTOR, "#back-to-products")
    TITLE = (By.CSS_SELECTOR, ".inventory_details_name")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product(self):
        self.click(self.ADD_TO_CART)


    def back_to_products(self):
        self.click(self.BACK)

    def get_product_title(self):
        title =  self.get_text(self.TITLE)
        return title

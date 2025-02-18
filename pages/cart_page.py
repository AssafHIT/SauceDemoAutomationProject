from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):

    _CHECKOUT_BTN = (By.CSS_SELECTOR, "#checkout")
    _FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    _LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    _ZIP = (By.CSS_SELECTOR, "#postal-code")
    _CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    _FINISH_BTN = (By.CSS_SELECTOR, "#finish")
    _PRODUCTS_TITLES = (By.CSS_SELECTOR, ".inventory_item_name")
    _CART_ITEMS = (By.CSS_SELECTOR, ".cart_item_label")
    _REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove-']")
    _CHECKOUT_MESSAGE = (By.CSS_SELECTOR, "#checkout_complete_container h2")
    _CHECKOUT_INFO_ERROR_MSG = (By.CSS_SELECTOR, ".checkout_info h3")

    def __init__(self, driver):
        super().__init__(driver)

    def checkout(self):
        self.click(self._CHECKOUT_BTN)

    def fill_info(self, firstname, lastname, zip):
        self.fill_text(self._FIRST_NAME, firstname)
        self.fill_text(self._LAST_NAME, lastname)
        self.fill_text(self._ZIP, zip)
        self.click(self._CONTINUE_BTN)
        try:
            # Wait for the Finish button to be clickable (timeout of 10 seconds)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self._FINISH_BTN)
            )
            # Click the Finish button
            self.click(self._FINISH_BTN)
        except Exception as e:
            print(f"Failed to click the Finish button: {e}")

    def get_products_titles(self):
        return [element.text for element in self.driver.find_elements(*self._PRODUCTS_TITLES)]


    def remove_item_by_index(self, index):
        cart_items = self.driver.find_elements(*self._CART_ITEMS)
        if index < 0 or index >= len(cart_items):
            raise IndexError(f"Invalid index: {index}")
        remove_buttons = self.driver.find_elements(*self._REMOVE_BUTTONS)
        remove_buttons[index].click()

    def get_cart_items(self):
        return self.driver.find_elements(*self._CART_ITEMS)

    def is_cart_empty(self):
        cart_items = self.get_cart_items()
        return len(cart_items) == 0

    def continue_click(self):
        self.click(self._CONTINUE_BTN)
    def finish_click(self):
        self.click(self._FINISH_BTN)

    def get_checkout_message(self):
        return self.get_text(self._CHECKOUT_MESSAGE)

    def get_info_error_message(self):
        return self.get_text(self._CHECKOUT_INFO_ERROR_MSG)

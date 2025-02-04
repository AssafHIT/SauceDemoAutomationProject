from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):

    CHECKOUT_BTN = (By.CSS_SELECTOR, "#checkout")
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    ZIP = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    FINISH_BTN = (By.CSS_SELECTOR, "#finish")
    PRODUCTS_TITLES = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item_label")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove-']")
    CHECKOUT_MESSAGE = (By.CSS_SELECTOR, "#checkout_complete_container h2")
    CHECKOUT_INFO_ERROR_MSG = (By.CSS_SELECTOR, ".checkout_info h3")



    def __init__(self, driver):
        super().__init__(driver)

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def fill_info(self, firstname, lastname, zip):
        self.fill_text(self.FIRST_NAME, firstname)
        self.fill_text(self.LAST_NAME, lastname)
        self.fill_text(self.ZIP, zip)
        self.click(self.CONTINUE_BTN)
        try:
            # Wait for the Finish button to be clickable (timeout of 10 seconds)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.FINISH_BTN)
            )
            # Click the Finish button
            self.click(self.FINISH_BTN)
        except Exception as e:
            print(f"Failed to click the Finish button: {e}")

    def get_products_titles(self):
        return [element.text for element in self.driver.find_elements(*self.PRODUCTS_TITLES)]


    def remove_item_by_index(self, index):
        cart_items = self.driver.find_elements(*self.CART_ITEMS)
        if index < 0 or index >= len(cart_items):
            raise IndexError(f"Invalid index: {index}")
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        remove_buttons[index].click()

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)

    def is_cart_empty(self):
        cart_items = self.get_cart_items()
        return len(cart_items) == 0

    def continue_click(self):
        self.click(self.CONTINUE_BTN)
    def finish_click(self):
        self.click(self.FINISH_BTN)

    def get_checkout_message(self):
        return self.get_text(self.CHECKOUT_MESSAGE)

    def get_info_error_message(self):
        return self.get_text(self.CHECKOUT_INFO_ERROR_MSG)

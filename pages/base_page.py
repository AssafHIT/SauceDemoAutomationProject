from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click(self, locator) -> None:
        """Wait for the element to be clickable and then click it."""
        try:
            # Wait for the element to be clickable
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(locator)
            )
            # Click the element once it's clickable
            self.driver.find_element(*locator).click()
        except Exception as e:
            print(f"Failed to click the element: {e}")

    def fill_text(self, locator, txt: str) -> None:
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(txt)

    def get_text(self, locator) -> str:
        return self.driver.find_element(*locator).text
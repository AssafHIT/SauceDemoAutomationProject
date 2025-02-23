import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def highlight_element(self, locator, color: str):
        element = self.driver.find_element(*locator)
        # Store the original style (to revert after)
        original_style = element.get_attribute("style")
        # Create the new style
        new_style = f"background-color: {color}; {original_style}"

        # Apply new style
        self.driver.execute_script("""
                      var element = arguments[0];
                      var new_style = arguments[1];
                      setTimeout(function() {
                          element.setAttribute('style', new_style);
                      }, 0);
                  """, element, new_style)

        # Revert to the original style after a short 300 mills
        self.driver.execute_script("""
              var element = arguments[0];
              var originalStyle = arguments[1];
              setTimeout(function() {
                  element.setAttribute('style', originalStyle);
              }, 300);
          """, element, original_style)


    def click(self, locator) -> None:
        self.highlight_element(locator, "Yellow")
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
        self.highlight_element(locator, "Yellow")
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(txt)
        time.sleep(1)

    def get_text(self, locator) -> str:
        self.highlight_element(locator, "Orange")
        return self.driver.find_element(*locator).text

    def hover_over_element(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).perform()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def take_screenshot(self, file_name="screenshot.png"):
        self.driver.save_screenshot(file_name)

    def is_element_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False
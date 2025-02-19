from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def highlight_element(self, locator, color: str):
        # Find the element
        element = self.driver.find_element(*locator)
        # Store the original style (to revert after 300 mills)
        original_style = element.get_attribute("style")

        # Create the new style with the given color
        new_style = f"background-color: {color}; {original_style}"

        # Apply the new style
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

    def get_text(self, locator) -> str:
        self.highlight_element(locator, "Orange")
        return self.driver.find_element(*locator).text




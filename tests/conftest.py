import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class", autouse=True)
def setup(request):
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield
    driver.quit()

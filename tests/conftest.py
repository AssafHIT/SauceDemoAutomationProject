import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage
from pages.item_page import ItemPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


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

@pytest.fixture(scope="function")
def driver():
    """Fixture to set up and tear down WebDriver."""
    options = Options()
    options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver  # Provide the WebDriver instance to the test

    driver.quit()  # Close browser after test

@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope="function")
def products_page(driver):
    return ProductsPage(driver)

@pytest.fixture(scope="function")
def item_page(driver):
    return ItemPage(driver)

@pytest.fixture(scope="function")
def cart_page(driver):
    return CartPage(driver)
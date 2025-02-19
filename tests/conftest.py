import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage
from pages.item_page import ItemPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.fixture(scope="function")
def setup():
    """Fixture to set up and tear down WebDriver."""
    options = Options()
    options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_page(setup):
    return LoginPage(setup)

@pytest.fixture(scope="function")
def products_page(setup):
    return ProductsPage(setup)

@pytest.fixture(scope="function")
def item_page(setup):
    return ItemPage(setup)

@pytest.fixture(scope="function")
def cart_page(setup):
    return CartPage(setup)
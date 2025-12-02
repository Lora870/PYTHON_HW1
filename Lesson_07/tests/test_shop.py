import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_shop(driver):
    auth = AuthPage(driver)
    auth.login('standard_user', 'secret_sauce')
    auth.login_button()

    main = MainPage(driver)
    main.selection_of_product()
    main.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    order = OrderPage(driver)
    order.information_of_buyer('Natalya', 'Pozdnyakova', '6239128745')
    order.button_continue()
    total = order.get_result()

    assert total == '$58.29'
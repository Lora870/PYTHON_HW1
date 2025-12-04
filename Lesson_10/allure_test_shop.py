import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.allure_auth_page import AuthPage
from pages.allure_main_page import MainPage
from pages.allure_cart_page import CartPage
from pages.allure_order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@allure.title("Цикл покупки товара")
@allure.description("""
End-to-end тест, проверяющий полный процесс покупки в интернет-магазине:
1. Авторизация покупателя
2. Добавление товаров в корзину
3. Переход в корзину и оформление заказа
4. Ввод информации о покупателе
5. Проверка итоговой суммы заказа
""")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    auth = AuthPage(driver)
    with allure.step("Ввод логина и пароля"):
        auth.login('standard_user', 'secret_sauce')
    with allure.step("Кликаем по кнопке 'Login'"):
        auth.login_button()

    main = MainPage(driver)
    with allure.step("Выбор товаров"):
        main.selection_of_product()
    with allure.step("Переход в корзину"):
        main.go_to_cart()

    with allure.step("Подтверждение состава корзины"):
        cart = CartPage(driver)
        cart.checkout()

    order = OrderPage(driver)
    with allure.step("Отправка данных покупателя"):
        order.information_of_buyer('Natalya', 'Pozdnyakova', '6239128745')
        order.button_continue()
    with allure.step("Получение итоговой суммы заказа"):
        total = order.get_result()
    with allure.step("Проверка итоговой суммы заказа"):
        assert total == '$58.29'
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    # при необходимости:
    # options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop_total_58_29(driver):
    wait = WebDriverWait(driver, 15)

    # 1. Открыть сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Логин standard_user / secret_sauce
    username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password = driver.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # ждем, пока откроется список товаров
    wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))

    # 3. Добавить в корзину три нужных товара
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейти в корзину
    driver.find_element(By.ID, "shopping_cart_container").click()
    wait.until(EC.visibility_of_element_located((By.ID, "cart_contents_container")))

    # 5. Нажать Checkout
    driver.find_element(By.ID, "checkout").click()

    # 6. Заполнить форму (имя, фамилия, индекс)
    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")

    first_name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    postal_code.send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    # 7. Считать итоговую сумму Total
    total_label = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_label.text

    # 8. Проверка
    assert "$58.29" in total_text
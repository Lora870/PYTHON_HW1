from selenium.webdriver.common.by import By
import allure

class CartPage:
    def __init__(self, driver):
        self._driver = driver

@allure.step("Клиr по кнопке 'Checkout' ")
def checkout (self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
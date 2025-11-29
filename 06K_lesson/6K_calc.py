import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 60)

    # ждем появления поля delay и вводим 45
    delay_input = wait.until(EC.visibility_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # кликаем по кнопкам 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # ожидаем, что на экране появится текст 15 (калькулятор считает с задержкой)
    display_locator = (By.CSS_SELECTOR, "div.screen")
    assert wait.until(EC.text_to_be_present_in_element(display_locator, "15"))
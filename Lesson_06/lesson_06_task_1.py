from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Шаг 1: Настройка драйвера Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Шаг 2: Переходим на страницу
    driver.get('http://uitestingplayground.com/ajax')

    # Шаг 3: Кликаем по синей кнопке (класс btn-primary)
    button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()
    driver.implicitly_wait(20)

    # Шаг 4: Ждём появления зелёной плашки и печатаем
    content = driver.find_element(By.CSS_SELECTOR, "#content")
    txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
    print(txt)

finally:
    driver.quit()
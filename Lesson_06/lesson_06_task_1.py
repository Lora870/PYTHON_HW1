from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Шаг 1: Настройка драйвера Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Шаг 2: Переходим на страницу
    driver.get('http://uitestingplayground.com/ajax')

    # Шаг 3: Кликаем по синей кнопке (класс btn-primary)
    button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()
    print("Кнопка кликнута! ⏳ Ждём AJAX...")

    # Шаг 4: Ждём появления зелёной плашки (класс ajax-content или success-msg)
    wait = WebDriverWait(driver, 10)  # До 10 сек
    green_banner = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ajax-content.success-msg')))  # Или.alert-success, проверь F12

    # Шаг 5: Получаем и выводим текст
    text = green_banner.text
    print(f"Текст из зелёной плашки: {text}")

    sleep(2)  # Пауза для просмотра

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
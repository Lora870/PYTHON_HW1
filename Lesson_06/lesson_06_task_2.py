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
driver.implicitly_wait(20)
try:
    # Шаг 2: Переходим на страницу
    driver.get('http://uitestingplayground.com/textinput')

    # Шаг 3: Находим поле ввода (id="my-input" или.form-control)
    input_field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')

    # Шаг 4: Вводим текст "SkyPro"
    input_field.clear()  # Очищаем, если нужно
    input_field.send_keys('SkyPro')
    print("Текст 'SkyPro' введён в поле! ✅")

    # Шаг 5: Кликаем по синей кнопке
    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()
    print("Кнопка кликнута! ⏳ Ждём обновления...")

    # Шаг 6: Ждём изменения кнопки и получаем текст
    # driver.implicitly_wait(20)
    txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(txt)
    sleep(2)  # Пауза для просмотра

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
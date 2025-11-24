from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service  # Для Firefox
from webdriver_manager.firefox import GeckoDriverManager  # Авто-скачивает geckodriver
from time import sleep

# Шаг 1: Настройка драйвера Firefox
service = Service(GeckoDriverManager().install())
# Или ручной: service = Service(r'C:\geckodriver\geckodriver.exe')  # Твой путь
driver = webdriver.Firefox(service=service)

try:
    # Шаг 2: Переходим на страницу
    driver.get('http://the-internet.herokuapp.com/inputs')

    # Шаг 3: Ждём загрузки
    sleep(5)

    # Шаг 4: Находим первое поле ввода (XPath: //input — первое поле)
    input_field = driver.find_element(By.XPATH, '//input')

    # Шаг 5: Вводим текст "Sky" (метод send_keys)
    input_field.send_keys('Sky')
    print("Текст 'Sky' введён в поле! ✅")
    sleep(3)
    input_field.clear()
    sleep(3)
    input_field.send_keys('Pro')
    print("Текст 'Pro' введён в поле! ✅")
    sleep(3)

    sleep(3)  # Пауза, чтобы увидеть (опционально)

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Шаг 6: Закрываем браузер
    driver.quit()
    print("Firefox закрыт! 🎉")
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import CalculatorPage

@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator_addition_with_delay(driver):
    """
    Тест калькулятора с задержкой
    Шаги:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Выполнить операцию 7 + 8
    4. Проверить, что результат равен 15
    """
    # 1. Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Создать объект страницы
    calculator_page = CalculatorPage(driver)

    # 3. Установить задержку
    calculator_page.set_delay("45")

    # 4. Выполнить операцию 7 + 8 =
    calculator_page.click_digit("7")
    calculator_page.click_operator("+")
    calculator_page.click_digit("8")
    calculator_page.click_equals()

    # 5. Ожидать результат и проверить его
    is_result_correct = calculator_page.wait_for_display_text("15")

    # 6. Assert проверка
    assert is_result_correct, f"Ожидался результат '15', но получен '{calculator_page.get_display_text()}'"


def test_calculator_addition_with_delay_alternative(driver):
    """Альтернативная версия теста с использованием метода perform_calculation"""
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator_page = CalculatorPage(driver)
    calculator_page.set_delay("45")

    # Используем метод для выполнения последовательности кнопок
    calculator_page.perform_calculation('7', '+', '8', '=')

    # Ожидаем результат
    assert calculator_page.wait_for_display_text("15"), \
        f"Результат не совпадает с ожидаемым. Текущий результат: {calculator_page.get_display_text()}"
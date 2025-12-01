import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page_enhanced import CalculatorPageEnhanced


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_7_plus_8_with_45_seconds_delay(driver):
    """Основной тест: 7 + 8 = 15 с задержкой 45 секунд"""
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator = CalculatorPageEnhanced(driver)

    # Устанавливаем задержку
    calculator.set_delay(45)

    # Выполняем вычисление
    calculator.calculate("7+8=")

    # Получаем и проверяем результат
    result = calculator.get_result()
    assert result == "15", f"Expected '15', got '{result}'"


def test_multiple_operations(driver):
    """Тест нескольких операций"""
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator = CalculatorPageEnhanced(driver)
    calculator.set_delay(5)

    # Тестируем различные операции
    test_cases = [
        ("2+3=", "5"),
        ("9-4=", "5"),
        ("6×3=", "18"),
        ("8÷2=", "4"),
    ]

    for expression, expected in test_cases:
        calculator.calculate(expression)
        assert calculator.wait_for_result(expected, 10), \
            f"Failed for {expression}. Expected {expected}"

        # Очищаем для следующего теста (предполагаем, что есть кнопка C)
        try:
            calculator.press_button("C")
        except:
            # Если нет кнопки C, обновляем страницу
            driver.refresh()
            calculator = CalculatorPageEnhanced(driver)
            calculator.set_delay(5)
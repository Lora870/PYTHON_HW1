import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page_enhanced import CalculatorPageEnhanced

@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
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
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """Общая фикстура для всех тестов"""
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # для запуска без UI

    # Автоматическая загрузка драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    # Скриншот при падении теста
    if hasattr(pytest, "test_failed") and pytest.test_failed:
        driver.save_screenshot("test_failure.png")

    driver.quit()
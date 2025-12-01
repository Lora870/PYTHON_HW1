from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Union


class CalculatorPageEnhanced:
    """Расширенная версия Page Object для калькулятора"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    # Основные локаторы
    DELAY_INPUT = (By.ID, "delay")
    DISPLAY = (By.CSS_SELECTOR, "div.screen")

    # Словарь с локаторами специальных кнопок
    SPECIAL_BUTTONS = {
        "equals": (By.XPATH, "//span[text()='=']"),
        "add": (By.XPATH, "//span[text()='+']"),
        "subtract": (By.XPATH, "//span[text()='-']"),
        "multiply": (By.XPATH, "//span[text()='×']"),
        "divide": (By.XPATH, "//span[text()='÷']"),
    }

    def _get_button_locator(self, button_value: str) -> tuple:
        """Возвращает локатор для кнопки"""
        # Проверяем, является ли кнопка специальной
        if button_value in self.SPECIAL_BUTTONS:
            return self.SPECIAL_BUTTONS[button_value]
        # Иначе считаем, что это цифра или обычная кнопка
        return (By.XPATH, f"//span[text()='{button_value}']")

    def set_delay(self, seconds: Union[str, int]) -> None:
        """Устанавливает задержку калькулятора"""
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_button(self, button_value: str) -> None:
        """Нажимает указанную кнопку"""
        locator = self._get_button_locator(button_value)
        button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        button.click()

    def press_buttons(self, buttons: List[str]) -> None:
        """Нажимает последовательность кнопок"""
        for button in buttons:
            self.press_button(button)

    def calculate(self, expression: str) -> None:
        """
        Выполняет вычисление по строковому выражению
        Пример: "7+8=" или "5*3="
        """
        for char in expression:
            self.press_button(char)

    def get_result(self, timeout: int = None) -> str:
        """
        Получает результат с экрана, ожидая его появления
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait

        # Ждем, пока на дисплее не появится непустой результат
        def result_is_ready(driver):
            display = driver.find_element(*self.DISPLAY)
            text = display.text.strip()
            return text if text and text != "" else False

        return wait.until(result_is_ready)

    def wait_for_result(self, expected_result: str, timeout: int = None) -> bool:
        """
        Ожидает появления определенного результата
        """
        try:
            wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
            return wait.until(
                EC.text_to_be_present_in_element(self.DISPLAY, expected_result)
            )
        except:
            return False
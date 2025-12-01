from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    # Локаторы
    DELAY_INPUT = (By.ID, "delay")
    DISPLAY = (By.CSS_SELECTOR, "div.screen")

    # Метод для получения локатора кнопки по тексту
    @staticmethod
    def _button_locator(button_text: str) -> tuple:
        return (By.XPATH, f"//span[text()='{button_text}']")

    # Методы для взаимодействия с элементами

    def set_delay(self, delay_value: str) -> None:
        """Устанавливает значение задержки в поле ввода"""
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def click_button(self, button_text: str) -> None:
        """Нажимает кнопку калькулятора по ее тексту"""
        button = self.driver.find_element(*self._button_locator(button_text))
        button.click()

    def click_digit(self, digit: str) -> None:
        """Нажимает цифровую кнопку"""
        self.click_button(digit)

    def click_operator(self, operator: str) -> None:
        """Нажимает кнопку оператора"""
        self.click_button(operator)

    def click_equals(self) -> None:
        """Нажимает кнопку равно"""
        self.click_button("=")

    def get_display_text(self) -> str:
        """Возвращает текст с дисплея калькулятора"""
        display = self.wait.until(
            EC.visibility_of_element_located(self.DISPLAY)
        )
        return display.text

    def wait_for_display_text(self, expected_text: str, timeout: int = None) -> bool:
        """
        Ожидает появления определенного текста на дисплее
        Возвращает True, если текст появился в течение таймаута
        """
        if timeout:
            wait = WebDriverWait(self.driver, timeout)
        else:
            wait = self.wait

        try:
            return wait.until(
                EC.text_to_be_present_in_element(self.DISPLAY, expected_text)
            )
        except:
            return False

    def perform_calculation(self, *buttons: str) -> None:
        """
        Выполняет последовательность нажатий кнопок
        Пример использования: perform_calculation('7', '+', '8', '=')
        """
        for button in buttons:
            self.click_button(button)
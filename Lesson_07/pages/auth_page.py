from selenium.webdriver.common.by import By


class AuthPage:
    def __init__(self, driver):
        self._driver = driver

    def login(self, username, password):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    def login_button(self):
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
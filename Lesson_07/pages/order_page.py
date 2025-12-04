from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, driver):
        self._driver = driver


    def information_of_buyer(self, first_name, last_name, code):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(code)

    def button_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def get_result(self):
        return  self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text.replace('Total: ', '')
        #total = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text.replace('Total: ', '')
        #total = total_text.replace('Total: ', '')
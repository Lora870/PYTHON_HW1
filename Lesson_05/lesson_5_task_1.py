from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
button.click()

print("Клик на синюю кнопку с CSS-классом выполнен успешно! ✅")

driver.quit()
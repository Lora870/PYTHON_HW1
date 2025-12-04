from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://the-internet.herokuapp.com/login")
sleep(2)

username_locator = '#username'
username_input = driver.find_element(By.CSS_SELECTOR, username_locator)
username_input.send_keys('tomsmith')
sleep(2)

password_locator = '#password'
password_input = driver.find_element(By.CSS_SELECTOR, password_locator)
password_input.send_keys('SuperSecretPassword!')
sleep(2)

button = driver.find_element(By.CSS_SELECTOR, 'button')
button.click()
sleep(2)

element = driver.find_element(By.CSS_SELECTOR, '.flash.success')
element_text = element.text
print(element_text)
sleep(2)

driver.quit()

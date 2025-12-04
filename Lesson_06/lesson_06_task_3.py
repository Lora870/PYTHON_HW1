from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# создаём драйвер (предполагается, что chromedriver в PATH)
driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Явное ожидание: все <img> на странице полностью загружены
    wait = WebDriverWait(driver, 20)
    wait.until(
        lambda d: d.execute_script(
            """
            const imgs = document.getElementsByTagName('img');
            if (imgs.length === 0) return false;
            for (let img of imgs) {
                if (!img.complete) return false;
            }
            return true;
            """
        )
    )

    # Находим все картинки и берём src у третьей (индекс 2)
    images = driver.find_elements(By.TAG_NAME, "img")
    third_image = images[2]
    src_value = third_image.get_attribute("src")

    print("SRC третьей картинки:", src_value)

finally:
    driver.quit()
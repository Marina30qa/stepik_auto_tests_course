import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
# Посчитать математическую функцию от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

button=browser.find_element(By.ID, "book")
button.click()

# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Найти х
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)


button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()
time.sleep(10)
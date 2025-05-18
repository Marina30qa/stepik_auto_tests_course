from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

# Посчитать математическую функцию от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# Нажать на кнопку
button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

# Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

# На новой странице решить капчу для роботов, чтобы получить число с ответом

# Считать значение для переменной x.
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()



time.sleep(10)

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math
# Посчитать математическую функцию от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.support.expected_conditions import new_window_is_opened

# Открыть страницу
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# Нажать на кнопку
button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

# Переключиться на новую вкладку браузера
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# Пройти капчу для робота и получить число-ответ

# Найти х
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

time.sleep(10)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
# Посчитать математическую функцию от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x.
    box = browser.find_element(By.ID, "treasure")
    x_element = box.get_attribute("valuex")
    x = x_element
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # Выбрать radiobutton "Robots rule!".
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
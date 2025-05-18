from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# Открыть страницу
try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменных x и y.
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text
    box = str(int(x)+int(y))

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(box)  # ищем элемент с результатом сложения

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
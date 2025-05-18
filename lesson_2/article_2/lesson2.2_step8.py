from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element(By.CSS_SELECTOR, '[name = "firstname"]')
input1.send_keys("Marina")

input2 = browser.find_element(By.CSS_SELECTOR, '[name = "lastname"]')
input2.send_keys("Sereda")

input3 = browser.find_element(By.CSS_SELECTOR, '[name = "email"]')
input3.send_keys("test@mail.ru")

# получаем путь к директории текущего исполняемого скрипта
current_dir = os.path.abspath(os.path.dirname(__file__))

# указываем имя файла, который будем загружать на сайт
file_name = "C:/Users/toporovama/PycharmProjects/AT_Education/lesson_2/article_2/file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)

element = browser.find_element(By.CSS_SELECTOR, '[type = "file"]')

# отправляем файл
element.send_keys(file_path)

# Нажать на кнопку Submit
button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]')
button.click()

time.sleep(15)

# импортируем модуль
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# получаем путь к директории текущего исполняемого скрипта
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "../../lesson_1/file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)

element = browser.find_element(By.CSS_SELECTOR, "[type='file']")

# отправляем файл
element.send_keys(file_path)

time.sleep(15)
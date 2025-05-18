from selenium import webdriver
import time

link = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

browser.execute_script("document.title='Script executing';alert('Robots at work');")
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(20)
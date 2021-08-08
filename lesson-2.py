from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x = browser.find_element_by_css_selector("div.form-group label span#input_value.nowrap")
    input_area = browser.find_element_by_css_selector("div.form-group input#answer,from-control")

    input_area.send_keys(calc(x.text))

    checkbox = browser.find_element_by_css_selector("div.form-check:nth-child(2) > label:nth-child(2)")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("div.form-check:nth-child(4) > label:nth-child(2)")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("form button.btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
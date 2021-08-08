from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим элемент с значением х
    x = browser.find_element_by_css_selector("form div.form-group label span#input_value.nowrap")
    #находим поле ввода
    input_area = browser.find_element_by_css_selector("div.form-group input#answer.form-control")
    #вводим в поле ввода ответ функции с аргментом значения х
    input_area.send_keys(calc(x.text))
    #находим кнопку элемента на странице
    button = browser.find_element_by_css_selector("form button.btn.btn-primary")
    #передаем js скрипт, который прокручивает страницу до кнопки
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #находим чекбокс и радио кнопки и кликаем по ним
    checkbox = browser.find_element_by_css_selector("div.form-check:nth-child(2) > label:nth-child(2)")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("form div.form-check.form-radio-custom label.form-check-label")
    radiobutton.click()

    # Отправляем заполненную форму
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

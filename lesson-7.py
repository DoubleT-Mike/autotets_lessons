from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #находим кнопку
    button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
    time.sleep(1)

    #нажимаем кнопку
    button.click()

    #получаем список окон браузера
    windows = browser.window_handles
    #переходим на последнию страницу
    browser.switch_to.window(windows[-1])


    #находим элемент с значением х
    x = browser.find_element_by_css_selector("div.form-group label span#input_value.nowrap")
 
    #находим поле ввода
    input_area = browser.find_element_by_css_selector("div.form-group input#answer.form-control")
    #вводим в поле ввода ответ функции с аргментом значения х
    input_area.send_keys(calc(x.text))

    #Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

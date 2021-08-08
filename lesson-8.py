from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим цену и ожидаем изминения до 100
    if WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    ):
        button = browser.find_element_by_css_selector("div.card div.card-body button#book.btn.btn-primary")
        # нажимаем кнопку
        button.click()

    # находим элемент с значением х
    x = browser.find_element_by_css_selector("div.form-group label span#input_value.nowrap")

    # находим поле ввода
    input_area = browser.find_element_by_css_selector("div.form-group input#answer.form-control")
    # вводим в поле ввода ответ функции с аргментом значения х
    input_area.send_keys(calc(x.text))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button#solve.btn.btn-primary")
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(20)
    browser.quit()

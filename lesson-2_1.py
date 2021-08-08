from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img_treasure = browser.find_element_by_css_selector("form div.form-group div div h2 img#treasure")

    img_treasure_attribute = img_treasure.get_attribute("valuex")
    calc(img_treasure_attribute)

    input_area = browser.find_element_by_css_selector("div.form-group input#answer,from-control")

    input_area.send_keys(calc(img_treasure_attribute))

    checkbox = browser.find_element_by_css_selector('form div.form-group div div input#robotCheckbox.check-input')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("form div.form-group div div input#robotsRule.check-input")
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

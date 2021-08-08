from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("html body.bg-light div.container form h2 span#num1.nowrap").text
    num2 = browser.find_element_by_css_selector("html body.bg-light div.container form h2 span#num2.nowrap").text

    select = Select(browser.find_element_by_css_selector("form div select#dropdown.custom-select"))
    select.select_by_visible_text(str(int(num1) + int(num2)))



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

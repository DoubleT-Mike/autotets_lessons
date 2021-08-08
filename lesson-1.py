from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    classes_list = ['first', 'second', 'third']
    for _class in classes_list:
        input = browser.find_element_by_css_selector(f"div.first_block div.form-group.{_class}_class input.form-control.{_class}") #очень уникальный селектор
        input.send_keys("text")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



    # input1 = browser.find_elements_by_css_selector('div.form-group input.form-control') # поиск обезательных к заполнению инпутов
    # for i in input1:
    #     if i.get_attribute("required"):
    #         i.send_keys("text")

    # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
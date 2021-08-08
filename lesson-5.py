from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    my_file = open("file.txt", "w+")
    my_file.close()

    input_area = browser.find_elements_by_css_selector("input[type='text']")

    for input in input_area:
        input.send_keys("random_text")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')

    loader = browser.find_element_by_css_selector("form input#file")
    loader.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("html body.bg-light div.container form button.btn.btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

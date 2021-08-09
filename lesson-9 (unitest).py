from selenium import webdriver
import time
import unittest

class Test_filling_in_reg_fields(unittest.TestCase):
    def test_1_filling_in_reg_fields(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        classes_list = ['first', 'second', 'third']
        for _class in classes_list:
            selector = f"div.first_block div.form-group.{_class}_class input.form-control.{_class}"
            input = browser.find_element_by_css_selector(selector)
            input.send_keys("text")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f'not find {_class} element')
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_2_filling_in_reg_fields(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        classes_list = ['first', 'second', 'third']
        for _class in classes_list:
            selector = f"div.first_block div.form-group.{_class}_class input.form-control.{_class}"
            input = browser.find_element_by_css_selector(selector)
            input.send_keys("text")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()


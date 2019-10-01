from selenium import webdriver
import time 
import unittest


class TestAbs(unittest.TestCase):
# Test 1.6.11
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector(".form-group.third_class .form-control.third")
        input3.send_keys("test@test.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(3)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text,1)

# Test 1.6.11_2

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector(".form-group.third_class .form-control.third")
        input3.send_keys("test@test.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(3)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text,1)


if __name__ == "__main__":
    unittest.main()

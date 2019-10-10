from selenium import webdriver
import time
#import pytest

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#    element = browser.find_element_by_css_selector('input[required].form-control.first')
    element = browser.find_element_by_css_selector('input[r1')
    element.send_keys("BigBudda")

    element = browser.find_element_by_css_selector('input[required].form-control.second')
    element.send_keys("BigBudda")

    element = browser.find_element_by_css_selector('input[required].form-control.third')
    element.send_keys("BigBudda")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

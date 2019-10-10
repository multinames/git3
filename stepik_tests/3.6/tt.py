from selenium import webdriver
import time
#import pytest

link = "http://stepik.org/lesson/236895/step/1/"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

#    element = browser.find_element_by_css_selector('input[required].form-control.first')
    element = browser.find_elements_by_tag_name('textarea')
    element.send_keys("BigBudda")

    button = browser.find_element_by_css_selector("submit-submission")
    button.click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()

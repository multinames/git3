from selenium import webdriver
import time
import math
#import pytest

answer = math.log(int(time.time()))

try:
    link = "http://stepik.org/lesson/236895/step/1/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    answer = math.log(int(time.time()))
#    print ("PRINT!",answer)

    input1 = browser.find_element_by_css_selector(".textarea")
#    input1 = browser.find_elements_by_tag_name('textarea')
#    input1 =  browser.find_element_by_xpath ("//textarea")
    input1.send_keys(answer)
    time.sleep(3)

    # send form
    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    # check in registration
    # waiting for loader
    time.sleep(1)

finally:
    # waiting
    time.sleep(10)
    # close 
    browser.quit()

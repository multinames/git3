from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class("quiz__typename")
    input1.send_keys("Ivan")

    time.sleep(2)

    # send form
    button = browser.find_element_by_class("submit-submission ")
    button.click()

    # check in registration
    # waiting for loader
    time.sleep(1)

finally:
    # waiting
    time.sleep(10)
    # close 
    browser.quit()

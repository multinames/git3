from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".form-group.third_class .form-control.third")
    input3.send_keys("test@test.com")

    # send form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # check in registration
    # waiting for loader
    time.sleep(1)

    # find elements
    welcome_text_elt = browser.find_element_by_tag_name("h1")

    # write text
    welcome_text = welcome_text_elt.text

    # check in
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # waiting
    time.sleep(10)
    # close 
    browser.quit()

import pytest
import time
import math

from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
#    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
#    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["stepik.org/lesson/236895/step/1","stepik.org/lesson/236896/step/1","stepik.org/lesson/236897/step/1","stepik.org/lesson/236898/step/1","stepik.org/lesson/236899/step/1","stepik.org/lesson/236903/step/1","stepik.org/lesson/236904/step/1","stepik.org/lesson/236905/step/1"])
def test_ufo(browser, url):

    link = f"https://{url}/"
    browser.implicitly_wait(5)
    browser.get(link)

    input1 =  browser.find_element_by_xpath ("//textarea")
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))

    # send form
    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    browser.implicitly_wait(3)
    correct = browser.find_element_by_css_selector(".smart-hints__hint")
#    correct = browser.find_element_by_xpath ("//pre[text()='Correct!']")
    browser.implicitly_wait(3)
    msg =  correct.text
    correct_msg = "Correct!"
    assert correct_msg == msg
#    print (msg)

#    time.sleep(2)

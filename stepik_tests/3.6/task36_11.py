import pytest
import time
import math

from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(5)
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["stepik.org/lesson/236895/step/1"])
def test_guest_should_see_login_link(browser, url):
    answer = math.log(int(time.time()))
    print(answer)
    link = f"https://{url}/"
    browser.get(link)
#    browser.find_element_by_css_selector("ember1598")
    input1 = browser.find_element_by_css_selector("quiz-component.ember-view")
    input1.send_keys(answer)
    

import pytest
import time
from selenium import webdriver


#@pytest.mark.parametrize('language')
def test_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(3)
    button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    print (button)
    time.sleep(5)

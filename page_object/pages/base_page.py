from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):    #метод (конструктор __init__)
        self.browser = browser           #экземпляр драйвера
        self.url = url                   #URL 
        self.browser.implicitly_wait(timeout) #неявное ожидание
        
    
    def open(self):                      #метод
        self.browser.get(self.url)       #открывает нужную страницу в браузере

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
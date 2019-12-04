class BasePage():
    def __init__(self, browser, url):    #метод (конструктор __init__)
        self.browser = browser           #экземпляр драйвера
        self.url = url                   #URL
        self.timeout = 5
    
    def open(self):                      #метод
        self.browser.get(self.url)
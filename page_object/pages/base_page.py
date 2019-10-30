class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.timeout = 5
    
    def open(self):
        self.browser.get(self.url)
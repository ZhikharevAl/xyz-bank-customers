



class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)

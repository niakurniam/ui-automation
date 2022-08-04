from selenium import webdriver

class Driver:
    def __init__(self):
        self.instance = webdriver.Chrome('../chromedriver_win32/chromedriver.exe')

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string")
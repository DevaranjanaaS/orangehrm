
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class BaseDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def quit(self):
        self.driver.quit()

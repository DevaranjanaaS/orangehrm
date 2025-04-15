
from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def login(self, username, password):
        self.wait.until(lambda d: d.find_element(By.NAME, LoginLocators.username)).send_keys(username)
        self.driver.find_element(By.NAME, LoginLocators.password).send_keys(password)
        self.driver.find_element(By.XPATH, LoginLocators.login_button).click()

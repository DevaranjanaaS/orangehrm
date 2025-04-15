
from selenium.webdriver.common.by import By
import time
from locators.dashboard_locators import DashboardLocators

class DashboardPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def logout(self):
        self.driver.find_element(By.XPATH, DashboardLocators.profile_icon).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, DashboardLocators.logout_link).click()
        print("🚪 Logged out.")

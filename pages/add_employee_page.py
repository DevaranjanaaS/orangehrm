
from selenium.webdriver.common.by import By
from locators.add_employee_locators import AddEmployeeLocators
import time

class AddEmployeePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def add_employee(self, first, last):
        self.wait.until(lambda d: d.find_element(By.NAME, AddEmployeeLocators.first_name)).send_keys(first)
        self.driver.find_element(By.NAME, AddEmployeeLocators.last_name).send_keys(last)
        self.driver.find_element(By.XPATH, AddEmployeeLocators.save_button).click()
        time.sleep(3)

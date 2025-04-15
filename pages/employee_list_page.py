
from selenium.webdriver.common.by import By
import time
from locators.employee_list_locators import EmployeeListLocators

class EmployeeListPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def search_employee(self, name):
        search_box = self.wait.until(lambda d: d.find_element(By.XPATH, EmployeeListLocators.search_input))
        search_box.clear()
        search_box.send_keys(name)
        time.sleep(2)
        rows = self.driver.find_elements(By.XPATH, EmployeeListLocators.result_rows)
        found = any(name in row.text for row in rows)
        if found:
            print(f"✅ Verified: {name}")
        else:
            print(f"❌ Not found: {name}")

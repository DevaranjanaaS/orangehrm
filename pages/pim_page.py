
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from locators.pim_locators import PIMLocators

class PIMPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def go_to_pim(self):
        pim_menu = self.wait.until(lambda d: d.find_element(By.XPATH, PIMLocators.pim_menu))
        ActionChains(self.driver).move_to_element(pim_menu).click().perform()
        time.sleep(2)

    def go_to_add_employee(self):
        self.driver.find_element(By.LINK_TEXT, PIMLocators.add_employee_link).click()
        time.sleep(2)

    def go_to_employee_list(self):
        self.driver.find_element(By.LINK_TEXT, PIMLocators.employee_list_link).click()
        time.sleep(3)

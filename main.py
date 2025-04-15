
from base_driver import BaseDriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage
import time

base = BaseDriver()
driver = base.driver
wait = base.wait

login = LoginPage(driver, wait)
dashboard = DashboardPage(driver, wait)
pim = PIMPage(driver, wait)
add_emp = AddEmployeePage(driver, wait)
emp_list = EmployeeListPage(driver, wait)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

login.login("Admin", "admin123")
pim.go_to_pim()

employee_data = [("Alice", "Wills"), ("Bob", "Marley"), ("Carol", "White")]

for first, last in employee_data:
    pim.go_to_add_employee()
    add_emp.add_employee(first, last)
    pim.go_to_pim()

pim.go_to_employee_list()

for first, _ in employee_data:
    emp_list.search_employee(first)

dashboard.logout()
base.quit()

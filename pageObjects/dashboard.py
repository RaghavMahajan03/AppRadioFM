# dashboard_page.py
from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_link = (By.CSS_SELECTOR, "a.row[href='/dashboard']")

    def go_to_dashboard(self):
        self.driver.find_element(*self.dashboard_link).click()

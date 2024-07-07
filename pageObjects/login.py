from selenium.webdriver.common.by import By


class LogIn:
    def __init__(self, driver):
        self.driver = driver
        self.signup_link = (By.XPATH, "//a[@href='/signup']")

    def go_to_signup(self):
        self.driver.find_element(*self.signup_link).click()

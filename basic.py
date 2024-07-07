import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# driver.find_element(By.ID,"autosuggest").send_keys("ind")
# time.sleep(5)
# countries = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# print(len(countries))
#
# for country in countries:
#     if country.get_attribute("value") == "option2":
#         country.click()
#         assert country.is_selected()
#         break

countries = driver.find_elements(By.XPATH,"//input[@class='radioButton']")
print(len(countries))

for country in countries:
    if country.get_attribute("value") == "radio2":
        country.click()
        assert country.is_selected()
        break

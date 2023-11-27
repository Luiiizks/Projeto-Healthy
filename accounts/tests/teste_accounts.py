from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://web-application-healthy.azurewebsites.net/")

create_account_link = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Create Account"))
)
create_account_link.click()

time.sleep(5)

username = "teste"
driver.find_element(By.NAME, "username").send_keys(username)
password = "12345678"
driver.find_element(By.NAME, "password1").send_keys(password)
driver.find_element(By.NAME, "password2").send_keys(password)



# Adjust the code to locate the button by its ID
def register_button (self,driver):
    register = driver.find_element(By.ID, "button_register")
    register_button.click()
    print('ok')
    time.sleep(10)



def run_tests(self, driver):
    self.register(driver)


print("passou")

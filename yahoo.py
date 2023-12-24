import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://login.yahoo.com/account/create")

# first_name
driver.find_element(By.ID, "usernamereg-firstName").send_keys("mahdi")

# last_name
driver.find_element(By.ID, "usernamereg-lastName").send_keys("norouzi")

# email
driver.find_element(By.ID, "usernamereg-userId").send_keys('test@gmail.com')

# password
driver.find_element(By.ID, "usernamereg-password").send_keys('1234')

time.sleep(5)

# signup
signup_btn = driver.find_element(By.NAME, "signup")
signup_btn.click()

input("Press any key to continue...")

driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.google.com')

# pass first page modal
driver.find_element(By.ID, 'vc3jof').click()
driver.find_element(By.CLASS_NAME, 'Ge0Aub').click()
driver.find_element(By.ID, "W0wltc").click()

# search place
driver.find_element(By.ID, "APjFqb").send_keys("how to use selenium in python" + Keys.ENTER)

input('Press any key to continue...')

driver.quit()

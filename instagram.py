import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.instagram.com')

input('press enter to start: ')

username = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
username.send_keys(input('enter username: '))

password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(input('enter password: ') + Keys.ENTER)

search_list = input('enter your search items(separate with ,): ').split(',')

for item in search_list:
    if item.startswith('#'):
        driver.get(f'https://www.instagram.com/explore/tags/{item[1:]}/')
    else:
        driver.get(f'https://www.instagram.com/{item}/')

input('press enter to exit: ')
driver.quit()

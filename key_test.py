import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://en.key-test.ru/")

modal_btn = driver.find_element(By.CLASS_NAME, 'fc-close')
# action.click(modal_btn).perform()
modal_btn.click()

footer_btn = driver.find_element(By.CLASS_NAME, 'cookie__ok')
# action.click(footer_btn).perform()
footer_btn.click()


# driver.find_element(By.CLASS_NAME, 'tab__wrapper').send_keys(Keys.ENTER)
body = driver.find_element(By.TAG_NAME, 'body')
key_list = [Keys.ENTER, Keys.LEFT, Keys.RIGHT, Keys.UP, Keys.DOWN, Keys.ARROW_DOWN]

for item in key_list:
    time.sleep(2)
    body.send_keys(item)

time.sleep(3)

input('exit??')

driver.quit()

import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from colorama import init, Style, Fore
# TODO: not completed

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
# driver.find_element(By.CLASS_NAME, "_ain3 _9vcv _advm").send_keys(Keys.ENTER)

input('run?')

os.system('clear')
init()
Message = input(Fore.LIGHTCYAN_EX + 'Enter a message: ' + Fore.WHITE + Style.BRIGHT)
time.sleep(1)
Names = input(Fore.LIGHTCYAN_EX + 'enter your names(separated by commas): ' + Fore.WHITE).split(',')
time.sleep(1)
NumberRange = int(input(Fore.LIGHTCYAN_EX + 'enter number range: ' + Fore.WHITE))
time.sleep(1)

for name in Names:
    # driver.get('https://web.whatsapp.com/')
    # time.sleep(3)
    # driver.find_element(By.XPATH, '//*[@id="u_0_6_Mu"]').send_keys(Keys.ENTER)
    # time.sleep(1)
    driver.find_element(By.XPATH, '//div[@title=Search input textbox]').send_keys(name + Keys.ENTER)
input('exit?')

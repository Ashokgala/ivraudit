from selenium import webdriver
from getpass import getpass
import time
import os

from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.utils import keys_to_typing

driver = webdriver.Chrome('chromedriver.exe')


driver.get('https://192.168.0.37:8080/web/system.php/login/welcome')
flag = True
for i in range(100):
    if(flag):
        try:
            advanced = driver.find_element_by_css_selector('#details-button')
            advanced.click()
            break

        except:
            print('Not found')

            time.sleep(1.0)



flag = True
for i in range(100):
    if(flag):
        try:
            advanced = driver.find_element_by_id('proceed-link')
            advanced.click()
            break

        except:
            print('Not found')

            time.sleep(1.0)


for i in range(100):
    if(flag):
        try:
            username = driver.find_element_by_name('login_id')
            username.send_keys('ITNEW')
            break

        except:
            print('Not found')

            time.sleep(1.0)

for i in range(100):
    if(flag):
        try:
            password = driver.find_element_by_name('login_password')
            password.send_keys('ITNEW')
            password.send_keys(Keys.RETURN)
            break

        except:
            print('Not found')

            time.sleep(1.0)


campaigntickbox = driver.find_element_by_link_text('Voicelogs')
time.sleep(5.0)
campaigntickbox.send_keys(Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.SPACE)
input()
time.sleep(3.0)
date = driver.find_element_by_link_text('Voicelogs')
campaigntickbox.send_keys(Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.BACKSPACE,'01-01-2022',Keys.TAB,Keys.TAB,Keys.TAB,Keys.BACKSPACE,'01-05-2022',Keys.TAB,'12',Keys.TAB,'00',Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.SPACE)


input()
time.sleep(10.0)

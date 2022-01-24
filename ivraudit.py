

from getpass import getpass
from tkinter import N
from click import edit
from selenium import webdriver

import time
import os

from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.utils import keys_to_typing
import os

if(not os.path.exists('result.txt')):
    file = open('result.txt','w')
    file.write('IVR_NAME  Current Time ')
    file.close()


m = 0
f = open('ivr.txt','r')
z = f.read()
f.close()


z = z.split('\n')
z.pop()

os.system('cls')
#print(z)

flag = 0

#print(z)

ivrname = z[m]
# print(ivrname)
# input()
# os.system('cls')
#print(ivrname)
# input()



# os.system('cls')

username = 'ITNEW'
passw = "ITNEW"
# username = 'user10'
# passw = "user10"

driver = webdriver.Chrome('chromedriver.exe')

driver.get('http://192.168.0.201:8888/app/')

time.sleep(20.0)

username_text = driver.find_element_by_id('gwt-uid-1')
username_text.send_keys(username)


pwd_text = driver.find_element_by_id('gwt-uid-2')
pwd_text.send_keys(passw)
pwd_text.send_keys(Keys.RETURN)
time.sleep(8.0)
try:
    okbutton = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[3]/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div[3]/button[1]/span')
    okbutton.click()
except:
    print('Going onn without forced login')

time.sleep(15.0)


cancelextension = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[6]/div[2]/div/div[4]/button[2]/span')
cancelextension.click()

time.sleep(10.0)

manage = driver.find_element_by_link_text('Manage')
manage.click()

time.sleep(5.0)
# os.system('cls')
prompts = driver.find_element_by_link_text('Prompt')
prompts.click()

time.sleep(5.0)
print(ivrname)

search = driver.find_element_by_xpath("/html/body/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/input")

#print("Element is visible ? " + str(search.is_displayed()))

search.send_keys(Keys.SPACE)

search.send_keys(ivrname)
search.send_keys(Keys.RETURN)

edit1 = driver.find_element_by_xpath('//*[@id="col8"]/div/button/i')
edit1.click()


duration = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[5]/div[2]/div[5]/div/div/div/div/div[1]/div/audio')
#print(duration)
time.sleep(8.0)

duration.send_keys(Keys.TAB,Keys.TAB,Keys.SPACE)
time.sleep(3.0)
duration.send_keys(Keys.SPACE)
time.sleep(3.0)

var = duration.get_attribute('currentTime')

print("below is the current time")

print(var)

file = open('result.txt','a')
file.write('\n')
file.write(ivrname +":"+ var)
file.close()

file = open('result.txt','r')

print(file.read())

file.close()



cancelbutton = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[5]/div[3]/button[2]/span')
cancelbutton.click()


m+=1
time.sleep(8.0)

for i in range(len(z)):
    try:
        # os.system('cls')
        ivrname = z[m]
        m+=1
        manage = driver.find_element_by_link_text('Manage')
        manage.click()

        time.sleep(5.0)

        prompts = driver.find_element_by_link_text('Prompt')
        prompts.click()

        time.sleep(8.0)
        print(ivrname)

        search = driver.find_element_by_xpath("/html/body/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/input")

        #print("Element is visible ? " + str(search.is_displayed()))

        search.send_keys(Keys.CONTROL, 'a')

        search.send_keys(ivrname)
        search.send_keys(Keys.RETURN)
        time.sleep(3.0)

        edit1 = driver.find_element_by_xpath('//*[@id="col8"]/div/button/i')
        edit1.click()
        time.sleep(3.0)

        # edit1.send_keys(Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.TAB,Keys.SPACE)
        # time.sleep(2.0)

        # edit1.send_keys(Keys.SPACE)

        duration = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[5]/div[2]/div[5]/div/div/div/div/div[1]/div/audio')
        print(duration)
        time.sleep(8.0)

        duration.send_keys(Keys.TAB,Keys.TAB,Keys.SPACE)
        time.sleep(3.0)
        duration.send_keys(Keys.SPACE)
        time.sleep(3.0)

        var = duration.get_attribute('currentTime')

        print("below is the current time")

        file = open('result.txt','a')
        file.write('\n')
        file.write(ivrname +":"+ var)
        file.close()

        file = open('result.txt','r')

        print(file.read())

        file.close()


        

        # if count == m:


        #     f1 = open('result.txt','a')
        #     f1.write(ivrname, var)
        #     f1.write('\n')
        #     f1.close()

        # else :
        #     print("Unable to store the result in the file ! ! ")


        time.sleep(3.0) 


        cancelbutton = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[5]/div[3]/button[2]/span')
        cancelbutton.click()

        manage = driver.find_element_by_link_text('Manage')
        manage.click()

        time.sleep(5.0)
        # os.system('cls')
        prompts = driver.find_element_by_link_text('Prompt')
        prompts.click()

        time.sleep(5.0)
        print(ivrname)

        search = driver.find_element_by_xpath("/html/body/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/input")

        #print("Element is visible ? " + str(search.is_displayed()))

        search.send_keys(Keys.SPACE)

        search.send_keys(ivrname)
        search.send_keys(Keys.RETURN)

        



    except:

        print('I m done with work')



print(ivrname)

time.sleep(2.0)

m+=1

# input()


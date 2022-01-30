
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys

if(not os.path.exists('result.txt')):
    file = open('result.txt','w')
    file.write('IVR_NAME  :  Current Time ')
    file.close()

os.system('cls')

start = 0

import gspread
from oauth2client.service_account import ServiceAccountCredentials


try:

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    ss = client.open("IVR Auto-Audit Dump") # Open the spreadhseet
    sheet = ss.worksheet("Sheet1")  
    data = sheet.get_all_records()  
    count = 1
    
except:
    
    print("Error Detected in google sheets")
    time.sleep(10.0)
    
    
try:

    m = 0    
    f = open('ivr.txt','r')
    z = f.read()
    f.close()
    z = z.split('\n')
    z.pop()

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('http://192.168.0.201:8888/app/')
    time.sleep(8.0)
    username = 'ITNEW'
    passw = "ITNEW"
    ivrname = z[m]
    print(ivrname)

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

    time.sleep(10.0)
    
    cancelextension = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[6]/div[2]/div/div[4]/button[2]/span')
    cancelextension.click()
    
    time.sleep(8.0)
    
    manage = driver.find_element_by_link_text('Manage') 
    manage.click()
    
    time.sleep(3.0)
    
    prompts = driver.find_element_by_link_text('Prompt')
    prompts.click()
    
    time.sleep(3.0)
    
    search = driver.find_element_by_xpath("/html/body/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/input")
    search.send_keys(Keys.SPACE)
    search.send_keys(ivrname) 
    search.send_keys(Keys.RETURN)
    
    edit1 = driver.find_element_by_xpath('//*[@id="col8"]/div/button/i')
    edit1.click()
    
    duration = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[5]/div[2]/div[5]/div/div/div/div/div[1]/div/audio')
    time.sleep(8.0)
    duration.send_keys(Keys.TAB,Keys.TAB,Keys.SPACE)
    time.sleep(3.0)
    duration.send_keys(Keys.SPACE)
    
    time.sleep(40.0)
    var = duration.get_attribute('currentTime')
    
    print(var)
    
    file = open('result.txt','a') 
    file.write('\n')
    file.write(ivrname +":"+ var)
    file.close()
    file = open('result.txt','r')
    #print(file.read())
    file.close()
    
    append = sheet.append_row([ivrname, var])
    print(append)

    cancelbutton = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[5]/div[3]/button[2]/span')
    cancelbutton.click()

    m+=1

    time.sleep(8.0)

    for i in range(len(z)):

        try:

            ivrname = z[m]
            #m+=1
            manage = driver.find_element_by_link_text('Manage')
            manage.click()

            time.sleep(3.0)

            prompts = driver.find_element_by_link_text('Prompt')
            prompts.click()

            time.sleep(5.0)
            print(ivrname)

            search = driver.find_element_by_xpath("/html/body/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/input")
            search.send_keys(Keys.CONTROL, 'a')
            search.send_keys(ivrname)
            search.send_keys(Keys.RETURN)

            time.sleep(3.0)

            edit1 = driver.find_element_by_xpath('//*[@id="col8"]/div/button/i')
            edit1.click()

            time.sleep(3.0)
            duration = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[5]/div[2]/div[5]/div/div/div/div/div[1]/div/audio')
            print(duration)

            time.sleep(5.0)

            duration.send_keys(Keys.TAB,Keys.TAB,Keys.SPACE)
            time.sleep(3.0)
            duration.send_keys(Keys.SPACE)
            time.sleep(40.0)

            var = duration.get_attribute('currentTime')

            file = open('result.txt','a')
            file.write('\n')
            file.write(ivrname +":"+ var)
            file.close()
            file = open('result.txt','r')
            #print(file.read())
            file.close()

            append = sheet.append_row([ivrname, var])
            print(append)
            time.sleep(3.0) 

            cancelbutton = driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[5]/div[3]/button[2]/span')
            cancelbutton.click()

            manage = driver.find_element_by_link_text('Manage')
            manage.click()

            time.sleep(3.0)
            prompts = driver.find_element_by_link_text('Prompt')
            prompts.click()
            time.sleep(3.0)

            print(ivrname)
            search = driver.find_element_by_xpath("/html/body/div[4]/div/div/main/div[3]/div/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/input")
            search.send_keys(Keys.SPACE)
            search.send_keys(ivrname)
            search.send_keys(Keys.RETURN)

        except:

            print('I m done with work all ivrs have been audited successfully')

        print(ivrname)
        time.sleep(2.0)
        m+=1

except:

    print('Something Went Wrong ! Pls check ashok ')








# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 20:15:05 2019

@author: Shaheer Akram
"""

import time as t
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re

path = "C:\\work\\chromedriver.exe"            #driver path here
driver = webdriver.Chrome(path)
url = "https://mbasic.facebook.com/messages/?pagination_direction=2&pageID=286392435175065&timestamp=1550836046267&see_older_newer=1&cursor&refid=11"        #link for messages


driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_name('email').send_keys("")      #email here
driver.find_element_by_name("pass").send_keys("")       #password here
driver.find_element_by_name("login").click()

driver.get(url)
driver.implicitly_wait(10)
body = driver.find_element_by_tag_name('body')

html = driver.page_source
data = soup(html)
message_list = data.find_all('table',{'class':'_5b6o _55wp _67ix _2ycx acw del_area async_del abb'})
#message_list = data.find_all('table',{'class':'bq br bs bt e bu bv bw'})
messages = []
reply = []
i = 1

links = data.find_all('h3',{'class':'_52je _52jg _5tg_'})

names = []
try:
    for i in range(100):
        for name in links:
            names.append(name.text.replace('\n',' ').strip())
            i=i+1
            if (i%10 == 0):
                driver.find_element_by_link_text('See Older Messages').click()
                driver.implicitly_wait(10)
                html = driver.page_source
                data = soup(html)
                links = data.find_all('h3',{'class':'_52je _52jg _5tg_'})
except:
   pass 
messages = []
reply = []

i = 0
print(len(names))

driver.get(url)
driver.implicitly_wait(10)


try:
    for i in range(len(names)):
        driver.find_element_by_link_text(names[i]).click()
        try:
            j = 0
            for j in range(100):
                driver.find_element_by_link_text('See Older Messages').click()
                driver.implicitly_wait(10)
                html = driver.page_source
                data = soup(html)
        except :
            try:
                for messege in data.find_all('div',{'class':'acw apl abt'}):
                    msg = messege.text.replace('\n',' ').strip()
                    print(msg)
                    messages.append(msg)
                for messege in data.find_all('div',{'id':'fua'}):
                    replies = messege.text.replace("\n"," ").strip()
                    print(replies)
                    reply.append(replies)
            except:
                driver.find_element_by_link_text('See Newer Messages').click()
                driver.implicitly_wait(10)
                html = driver.page_source
                data = soup(html)
            driver.get(url)
            driver.implicitly_wait(10)
            i = i+1
            if(i%10 == 0):
                driver.find_element_by_link_text('See Older Messages')
                driver.implicitly_wait(10)
            html = driver.page_source
            data = soup(html)

except Exception as e:
    print(e)
    pass
'''    
for item in message_list:
    driver.find_element_by_link_text(names[i]).click()
    for messages in data.find_all('span',{"class":'e bs bt'}):
        msg = messages.text.replace("\n"," ").strip()
        print(msg)
        messages.append(msg)
    for reply in data.find_all('span',{'id':'fua'}):
        replies = reply.text.replace("\n"," ").strip()
        print(reply)
        reply.append(replies)
    driver.back()		

    i=i+1
    if (i%10 == 0):
        driver.find_element_by_link_text('See Older Messages').click()
        html = driver.page_source
        data = soup(html)
        message_list = data.find_all('table',{'class':'_5b6o _55wp _67ix _2ycx acw del_area async_del abb'})

'''        
driver.close()
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:14:35 2018

@author: Shaheer Akram
"""

import time as t
from bs4 import BeautifulSoup as soup
#!pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import io
import pandas as pd

path = "C:\\Work\\chromedriver.exe"
driver = webdriver.Chrome(path)

body = driver.find_element_by_tag_name('body')

url = "" #Enter any twitter page 

clean = []

driver.get(url)
driver.implicitly_wait(10)

body = driver.find_element_by_tag_name('body')


for i in range(1000):
    #print(i)
    body.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(10)
    

html = driver.page_source
data = soup(html)
all_tweets = data.find_all('div',{'class':'tweet'})

for tweet in all_tweets:
        content = tweet.find('div',{'class':'content'})
        message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
        clean.append(message)
    

      
clean = list(set(clean))
dataFrame = pd.DataFrame(clean)
dataFrame.to_csv("tweets.csv")
driver.close()
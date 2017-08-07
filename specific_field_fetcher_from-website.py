# -------------------fetch fields froma website using a website url--------------------------------------------
# import libraries--- 
# to fetch webpage ---urllib, requests,to parse html webpage----bs4 n lxml 
# to use regular expression---re, to read from csv and write to csv ---csv and pandas.
# to automate the procedure of opening a website and achieving a task (eg. scrapping website/ logging into a webite)---Selenium(python)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests,re
import bs4 as bs
import csv
import lxml
# path to identify selenium chrome drive in your system
path_to_chrome = 'C:/Users/AliImran/Downloads/chromedriver_win32 (1)/chromedriver'
# open a website using selenium webdrive
browser=webdriver.Chrome(executable_path = path_to_chrome)
# create variables to store the fetched data in list and dictionary
angel_all={}
comp_location=[]
url='https://angel.co/companies'
i=0
# open a webpage using selenium python
browser.get(url)
# sleep for 3 sec to let the page load
time.sleep(3)
num=20
# j=0
# loop through the more button to display result from all the pages(pagination)
while num<=400:
	try:
		more_button=browser.find_element_by_css_selector('div.more')
		more_button.click()
		time.sleep(2)
	except:
		break
	num+=20
# to extract the required field, identify specific element locator from the webpage-- using inspect element
# use id/class/css selector/xpath
# use those locators as follows to extact required fields and store them in variables

all_comp_loc=browser.find_elements_by_css_selector('div.column.location div.value div a')

# loop through the variables to extract and append them to a variable list

for loc in all_comp_loc:
	loc_text=(loc.text)
	try:
		if len(loc_text)<=1:
			loc_text='Null'
			comp_location.append(loc_text)
		else:
			comp_location.append(loc_text)
	except:
		continue
# update the list into a dictionary
angel_all.update({'Location': comp_location})
# get the dictionary in a dataframe format using pandas
df= pd.DataFrame(angel_all)
# drop duplicates
df_nod=df.drop_duplicates()
# write the dataframe into csv file
df.to_csv('angel_UAE_startups_city_info-fetch.csv', index=False, encoding="UTF-8")
print df_nod
print 'Done!!'
# done!!!!!!!!
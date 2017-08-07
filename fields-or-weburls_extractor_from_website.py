# ---------------------Give main website urls csv file as input to fetch required fields from the website---------------------------
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
comp_names=[]
comp_location=[]
comp_website=[]
# Opening a csv file and reading the specific coulmn required
# here csv file with website urls are given as input to fetch required fields from the webpages in a variable

df = pd.read_csv('angel_UAE_startups_city_info-fetch-urls.csv', sep=',', header='infer')
urls = df.Website
i=0
# using exception handling to avoid any interruption due to error while running!!
# loop through the variable with urls and open a webpage using selenium python
for url in urls:
	print url
	try:
		browser.get(url)
		time.sleep(3)
	except:
		continue
	num=20
	j=0
# loop through the more button to display result from all the pages
	while True:
		try:
			more_button=browser.find_element_by_css_selector('div.more')
			more_button.click()
			time.sleep(2)
		except:
			break
    	num+=20
    	j+=20
    	# print j
# to extract the required field, identify specific element locator from the webpage-- using inspect element
# use id/class/css selector/xpath
# use those locators as follows to extact required fields and store them in variables
	all_comp_names=browser.find_elements_by_css_selector('div.name')
	all_comp_loc=browser.find_elements_by_css_selector('div.column.location div.value div a')
	all_links=browser.find_elements_by_css_selector('div.website a')
# loop through the variables to extract and append them to a variable list
	for name in all_comp_names:
		name_text=(name.text)
		try:
			if len(name_text)<=1:
				name_text='Null'
				comp_names.append(name_text)
			else:
				comp_names.append(name_text)
		except:
			continue
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
	for link in all_links:
		link_href=(link.get_attribute('href'))
		try:
			if link_href==None:
				link_href='Null'
				comp_website.append(link_href)
			else:
				comp_website.append(link_href)
		except:
			continue
# update those list into a dictionary
	angel_all.update({'Company Name' : comp_names,'Location': comp_location,'Website' : comp_website })
# get the dictionary in a dataframe format using pandas
	df= pd.DataFrame.from_dict(angel_all, orient='index')
	angel_info=df.transpose()
# drop duplicates
	angel_info_nod=angel_info.drop_duplicates()
write it to csv 
	angel_info_nod.to_csv('angel_UAE_clw_5-05.csv', index=False, encoding="UTF-8")
	i+=1
	print i
	# if i==20:
	# 	break
print 'done!'
# done..


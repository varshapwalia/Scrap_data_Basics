# -----------------------Give main website urls csv file as input to fetch inner contact page urls from the website---------------------------
# import libraries--- 
# to fetch webpage ---urllib, requests,to parse html webpage----bs4 n lxml 
# to use regular expression---re, to read from csv and write to csv ---csv and pandas.

import requests,re
import bs4 as bs
import time
import csv
import lxml
import pandas as pd

# create variables to store the fetched data in list and dictionary
all_mainpg_urls=[]
main_pg_url={}


# create variables to assign an wanted value(which are used to fetch 'SPECIFIC LINKS' containing them)
x='contact'

# Opening a csv file and reading the specific coulmn required
# here csv file with website urls are given as input to fetch inner page urls (contact page) from the webpages
with open('angel_UAE_clw_5-05-nodups.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    i=1
    for row in reader:
        url = row['Website']
        print url
        print i
# using exception handling to avoid any interruption due to error while running!!
# to open a webpage using urllib library
        try:
            page = requests.get(url)
        except:
            continue
# parse the page content to find all 'a' tags(to fetch links)
        page_data=bs.BeautifulSoup(page.content, "lxml")
        page_data_urls=page_data.find_all('a')
# loop through to get href link from the 'a' tag and append it to a list
        for urls in page_data_urls:
            mainpg_urls=urls.get('href')
            if mainpg_urls is not None:
                if mainpg_urls.startswith('/'):
                    if x in mainpg_urls.lower():
                        mainpg_urls=str(url)+str(mainpg_urls)
                        all_mainpg_urls.append(mainpg_urls)
                elif mainpg_urls.startswith('http') or mainpg_urls.startswith('https'):
                    if x in mainpg_urls.lower():
                        all_mainpg_urls.append(mainpg_urls)
            else:
                pass

# use update function and add all the collected email ids in list from previous step to a dictionary

        main_pg_url.update({'Website': all_mainpg_urls})

# to create a dataframe of the dictionary using pandas

        df_main_pg_url=pd.DataFrame(main_pg_url)
# drop duplicates
        df_main_pg_url_nd=df_main_pg_url.drop_duplicates()
# write resultant dataframe to a csv file
        df_main_pg_url_nd.to_csv('angel_UAE_innerurl_5-05.csv', index=False, encoding="UTF-8")
        i+=1
    print len(df_main_pg_url_nd)
        # if i>=10:
            # break
print 'done'
# done!!!!

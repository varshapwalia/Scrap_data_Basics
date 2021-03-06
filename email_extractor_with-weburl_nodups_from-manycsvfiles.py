# ----------------------give csv files with website urls as input to fetch email ids from the webpages----------------------------------

# import libraries--- 
# to fetch webpage ---urllib, to use regular expression---re, to read from csv and write to csv ---csv and pandas.

import urllib,re
import time
import csv
import pandas as pd

# create variables to store the fetched data in list and dictionary
email_ph_List={}
Phone=[]
Email=[]
noEmail=[]
web_url=[]

# create variables to assign an unwanted value(which are used to remove 'SPECIFIC STRING' containing them)

x='.jpg'
y='.png'

# Opening a csv file and reading the specific coulmn required
# here csv files with website urls are given as input to fetch email ids from the webpages

country_csvf_list=['angel_inner_urls_US_startups-alloc-2-05_nodups-corrected_del.csv', 'angel_mg_urls_US_startups-alloc-2-05.csv']
for c in country_csvf_list:
    with open("%s"%c) as csvfile:
        reader = csv.DictReader(csvfile)
        i=1
        for row in reader:
            url = row['Website']
            print url

# using exception handling to avoid any interruption due to error while running!!
# to open a webpage using urllib library

            try:
        	   page=urllib.urlopen(url)
            except:
            	page=''

# read the page content

            try:
                get_page=page.read()
            except:
                get_page=''
            if page=='':
                continue

# use regular expression to find all email ids in the webpage and store it in a variable

            try:
                email=re.findall(r"([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})",get_page)
            except:
                email='N' 

# loop through the variable and filter unwanted content and append the email ids to one of the list created in 2nd step

            for e in email:
            # web_url=[]
                if x in e or y in e:
                    e='Null'
                    Email.append(e)
                elif len(e)<=45:
                    Email.append(e)
                
                elif e is None:
                    e='Null'
                    Email.append(e)
                else:
                    e='Null'
                    Email.append(e)
                web_url.append(url)

# use update function and add all the collected email ids in list from previous step to a dictionary

            email_ph_List.update({'Website_url': web_url, 'Email_Id': Email})

# to create a dataframe in pandas
# use pandas dataframe function to reorient the created dictionary 
# and again use transpose function to change the orientation back 
# (the above steps are done to avoid error-- "arrays are of unequal length--- and pandas cannot process it")

            df= pd.DataFrame.from_dict(email_ph_List, orient='index')
            email_ph_List_info=df.transpose()

# remove any duplicates from the result

            nodups_df=email_ph_List_info.drop_duplicates()

# write the result to csv file
            nodups_df.to_csv('ANGEL_US_ALL_email_4-05_last_111_final_1.csv', index=False, encoding="UTF-8")
            print i 
            i+=1
            # if i==10:
            #     break

        print len(nodups_df)
    print len(nodups_df)

print len(nodups_df)
print 'done!'
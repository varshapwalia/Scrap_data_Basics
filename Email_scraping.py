import urllib.request,re
import ssl
import csv

a = []

with open('E:\downloads\software_startups.csv','r') as csvfile: #fetch data from csv
	plots=csv.reader(csvfile, delimiter=',')
	for row in plots:
		a.append(row[4]) #fill it in a list with the column that contains website urls

'''
#print verification
print(a)
# Websites which have email ids online or on website can be retrieved for eg these 2 websites. I dont know about the rest though. Maybe Beautiful Soup can do the trick.
# f = urllib.request.urlopen("https://pythonprogramming.net/")

#f = urllib.request.urlopen("http://www.thehotelwindsor.com.au/")
#g = urllib.request.urlopen("https://pythonprogramming.net/")

f = urllib.request.urlopen(a)
s = f.read().decode('utf-8')
#t = g.read().decode('utf-8')
print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s))
#print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",t))
'''
for temp in a:
	try:
		headers = {}
		headers['User-Agent'] = 'Mozilla/5.0 (X11;Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safaru/537.17'
		context = ssl._create_unverified_context()
		f = urllib.request.Request(str(temp), headers=headers)
		resp = urllib.request.urlopen(f,context=context)
		respData = resp.read().decode('utf-8')
		para = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",str(respData))
		for eachp in para:
			print(eachp)
	except Exception as e:
		pass
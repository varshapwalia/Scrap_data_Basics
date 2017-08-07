import re
import socket
import smtplib
import dns.resolver
import pandas as pd
import xlrd

def verify_address(email):
	print 1111111111112222
	print (email.Email)
	addressToVerify =email.Email
	match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

	if match == None:
		print('Bad Syntax')
		# raise ValueError('Bad Syntax')
		return 'Bad Syntax'

	print 6767



	records = dns.resolver.query('emailhippo.com', 'MX')
	print "email hippo entered"
	mxRecord = records[0].exchange
	mxRecord = str(mxRecord)


	print "entered 26 line"
	# Get local server hostname
	host = socket.gethostname()

	# SMTP lib setup (use debug level for full output)
	print 31
	server = smtplib.SMTP()
	print 35
	server.set_debuglevel(0)
	print 36
	# SMTP Conversation
	server.connect(mxRecord)
	print 40
	server.helo(host)
	print 42
	server.mail('me@domain.com')
	print 44
	code, message = server.rcpt(str(addressToVerify))
	print 46
	server.quit()
	print 11111111

	# Assume 250 as Success
	valid_or_not = ''
	if code == 250:
		print('Valid Email')
		valid_or_not = 'Valid'
	else:
		print('Invalid Email')
		valid_or_not = 'Invalid'
	return valid_or_not

df = pd.read_csv('Retal_B2b.csv')
# print (len(df))
df['Valid_or_not'] = df[2:500].apply(lambda row: verify_address(row),axis=1)
df.to_csv('RetalB2b9.csv',index=False)

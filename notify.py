#imports libraries
import urllib2
import re
import smtplib
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

html_content = urllib2.urlopen('http://sf.eater.com/neighborhood/oakland').read()
#defines html_content as the url to look through

matches = re.findall('The Shutter', html_content);
#looks for a string on the webpage

if len(matches) == 0: 
   print 'I did not find anything' #sys.exit() once script works to kill the script
else:
	fromaddr = "<insert from add here>" #sending addres
	toaddr = "<insert to add here>" #to address
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "New Shutter Article" #subject of the email
	 
	body = "Here is a link to the most recent Shutter article for [City]: " #body of the email
	msg.attach(MIMEText(body, 'plain'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "<insert password here>") # username/password
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
# git commit test
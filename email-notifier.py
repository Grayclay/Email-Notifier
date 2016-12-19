# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# Import regular expressions
import re 

import urllib2

import sys

from email.MIMEMultipart import MIMEMultipart

from email.MIMEText import MIMEText

#-----------------------------------------------------------

#scrape the page
url = "http://sf.eater.com/the-shutter"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)

#parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

#create an empty list
dates = []

#iterate through the parsed HTML and extract dates
for span_tag in soup.find_all("span"):
	if 'am' in span_tag.text:
		dates.append(span_tag.text)
	if 'pm' in span_tag.text:
		dates.append(span_tag.text)

#pull the last recorded article's date from a text file
with open("dates.txt", "r") as read_file:
	most_recent = read_file.readline()

if most_recent == dates[0]:
	sys.exit()
else:
	with open("dates.txt", "w") as write_file:
		write_file.write(dates[0])

	# email the results
	#sending addres
	fromaddr = "<insert from add here>" 
	#to address
	toaddr = "<insert to add here>" 
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	#subject of the email
	msg['Subject'] = "Shutter Article Check" 
	 
	 #body of the email
	body = "The most recent Shutter article page for SF Eater was posted on" + dates[0] + "Here is a link:  http://sf.eater.com/the-shutter" 
	msg.attach(MIMEText(body, 'plain'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "<insert password here>") # username/password
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
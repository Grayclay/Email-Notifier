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

for item in soup.find_all(attrs={'class': "m-entry-box__thumb "}):
	for link in item.find_all("a"):
		print link.get("href")
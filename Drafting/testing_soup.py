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

url = "http://sf.eater.com/the-shutter"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

dates = []

for item in soup.find_all(attrs={'class': 'p-byline__time'}):
	print item.string
	dates.append(item.string)
	
print dates
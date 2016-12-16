import urllib2
import re

html_content = urllib2.urlopen('http://sf.eater.com/neighborhood/oakland').read()

matches = re.findall('The Shutter', html_content);

if len(matches) == 0: 
   print 'I did not find anything'
else:
   print 'My string is in the html'

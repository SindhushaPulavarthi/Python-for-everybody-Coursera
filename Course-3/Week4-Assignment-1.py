import urllib.request 
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
#import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()#It will open the file and start reading
soup = BeautifulSoup(html, 'html.parser')#take all the nasty html and return all the good html and it returns a object to soup

# Retrieve all of the anchor tags
tags = soup('span')
#print(tags)
sum=0
for tag in tags:
	sum=(sum)+int((tag.contents[0]))

print(sum)
#digi=re.findall('[0-9]+',tag)
	#print(int(digi))


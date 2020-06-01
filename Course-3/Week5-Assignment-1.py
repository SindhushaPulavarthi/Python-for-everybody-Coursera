import urllib.request
import urllib.parse
import urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
#print('Retrieving', url)
html = urllib.request.urlopen(url, context=ctx)

data = html.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
data=data.decode()
tree=ET.fromstring(data)
lst=tree.findall('comments/comment')
sum=0
for item in lst:
    #print(item.find('count').text)
    sum=sum+int(item.find('count').text)
print(sum)

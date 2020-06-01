import urllib.request
import urllib.parse
import urllib.error
import ssl
import json

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
info=json.loads(data)
sum=0
#print (len(info["comments"]))
for i in range(0,len(info["comments"])):
    sum=sum+int(info["comments"][i]["count"])

print(sum)

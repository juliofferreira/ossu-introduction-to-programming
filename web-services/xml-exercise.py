import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Use the following URL: http://py4e-data.dr-chuck.net/comments_42.xml
url = input('Enter URL: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
data_string = data.decode()

tree = ET.fromstring(data_string)

counts = tree.findall('.//count')

total = 0

for count in counts:
    number = int(count.text)
    total += number

print(f'The sum is: {total}')
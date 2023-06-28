import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Use the following URL: http://py4e-data.dr-chuck.net/comments_42.json
url = input('Enter URL: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
data_string = data.decode()

info = json.loads(data_string)

total = 0

for comment in info['comments']:
    count = comment['count']
    total += count

print(f'Total: {total}')
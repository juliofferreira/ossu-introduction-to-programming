import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_url_content(url):
   print(f'Retrieving: {url}')
   html = urllib.request.urlopen(url, context=ctx).read()
   return BeautifulSoup(html, 'html.parser')

# Use the following URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count + 1):
   # Retrieve all of the anchor tags
   soup = get_url_content(url)
   tags = soup('a')
   next_url = tags[position - 1].get('href', None)
   url = next_url
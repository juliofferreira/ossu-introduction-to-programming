from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Use the following URL: http://py4e-data.dr-chuck.net/comments_42.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
total_sum = 0
for tag in tags:
   # Look at the parts of a tag
   number_int = int(tag.contents[0])
   total_sum += number_int

print(f"The sum is: {total_sum}")
# Objective: Learn how to webscrape using the
# http://web.mta.info/developers/turnstile.html website
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the url to the website and access the site with
# our requests library.
url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

# Check for appropriate website response: [200] means the
# connection went through successfully.
print(response)

soup = BeautifulSoup(response.text, "html.parser")
# Finds all lines that have the [a] tag.
soup.findAll('a')

one_a_tag = soup.findAll('a')[36]
link = one_a_tag['href']

# Download data from a website by appending the above link
# to the website link directory.
download_url = 'http://web.mta.info/developers/'+ link
# Use request.urlretrieve() to retrieve data from the above
# set url. First argument is the file url and the second
# argument is the filename we'll be saving it as.
# urllib.request.urlretrieve(\
#     download_url,'./'+link[link.find('/turnstile_')+1:])

# for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
#     one_a_tag = soup.findAll('a')[i]
#     link = one_a_tag['href']
#     download_url = 'http://web.mta.info/developers/'+ link
#     urllib.request.urlretrieve(download_url,'./downloaded_data/'+link[link.find('/turnstile_')+1:]) 
#     time.sleep(1) #pause the code for a sec
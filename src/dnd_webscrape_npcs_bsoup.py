# Get randomly generated NPCs
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://donjon.bin.sh/5e/random/#type=npc'
response = requests.get(url)
if str(response) == "<Response [200]>":
    print("Connection successful.")
else:
    print("ERROR: Cannot connect to donjon url.")
    print(response)

soup = BeautifulSoup(response.text, "html.parser")
single = soup.findAll('td')
#print(single.renderContents())
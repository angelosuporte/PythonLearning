from bs4 import BeautifulSoup

import requests

site = requests.get('https://www.climatempo.com.br/').content

soup = BeautifulSoup(site, 'html.parser')
#print(soup.prettify())
temp = soup.find("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")

print(temp.string)
print(soup.title.string)


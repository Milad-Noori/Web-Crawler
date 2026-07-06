import requests
from pyexpat import features

r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
# print(r)
# print(type(r))
# print(r.text)
# data = 'history' in r.text
# print(data)
import bs4
data = r.text
soup = bs4.BeautifulSoup(data,'html.parser')
# print(soup)
ti = soup.select("title")
# print (ti)
# print(type(ti))

div = soup.select('div')
# print(div)
# print(len(div))

# for item in soup.select('div'):
#     print(item.text)



# mat = soup.select('p.class')
# print(mat)
# 
# dclas = soup.select('div')
# 
# for item in dclas:
#     print(item.text)



# ----------------------------------------------------------------------------------------
import json

api_url = "http://api.open-notify.org/iss-now.json"

response = requests.get(api_url)

print(response)
print(response.text)
# print(response.json())
jason_data  = response.json()
print(jason_data)















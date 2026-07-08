import requests
from pyexpat import features

# r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
# print(r)
# print(type(r))
# print(r.text)
# data = 'history' in r.text
# print(data)
# import bs4
# data = r.text
# soup = bs4.BeautifulSoup(data,'html.parser')
# print(soup)
# ti = soup.select("title")
# print (ti)
# print(type(ti))

# div = soup.select('div')
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

# api_url = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(api_url)
#
# print(response)
# print(response.text)
# # print(response.json())
# jason_data  = response.json()
# print(jason_data)
#

# ------------------------------------------------------------------------------------------


# url_api = ""
# data= requests.get(url_api)
# print(data)
# text = data.text
# print(text)

# __________________________________________________________FlASK________________________________
# from flask import Flask
#
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return 'Hello, World!'
#
# @app.route('/about')
# def about():
#     return "this page is about"
#
# if __name__== 'main':
#     app.run()



link = requests.get("https://api.attackontitanapi.com/episodes")
print(link)
print(link.text)


























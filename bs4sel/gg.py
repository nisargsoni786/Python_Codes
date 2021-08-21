from bs4 import BeautifulSoup
from lxml import etree,html
import requests
import random

url="https://www.tuko.co.ke/339793-best-funny-jokes-a-girl-like.html"
req=requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")
dom=etree.HTML(str(soup))

data=[]

x=dom.xpath('/html/body/div[2]/div/div[2]/div[2]/section/section[1]/article/div[1]/ul[1]')
y=x[0].findall('li')
for i in range(len(y)):
    data.append(y[i].text)

x=dom.xpath('/html/body/div[2]/div/div[2]/div[2]/section/section[1]/article/div[1]/ul[2]')
y=x[0].findall('li')
for i in range(len(y)):
    data.append(y[i].text)

x=dom.xpath('/html/body/div[2]/div/div[2]/div[2]/section/section[1]/article/div[1]/ul[3]')
y=x[0].findall('li')
for i in range(len(y)):
    data.append(y[i].text)

print(len(data))
print(random.choice(data))
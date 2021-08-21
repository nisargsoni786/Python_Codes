from bs4 import BeautifulSoup
from lxml import etree
import requests

url="https://codewithharry.com/"
req=requests.get(url)
# print(req.text)

soup = BeautifulSoup(req.text, "html.parser")
dom=etree.HTML(str(soup))

# print(soup.prettify)
paras=soup.find_all('p')
# print(paras[0]['class'])

x=soup.find_all('p',class_='lead')
# print(x)

# print(x[0].text)
linksarr=[]
links=soup.find_all('a')
for link in links:
    linksarr.append(link.get('href'))

x=soup.find(id='signupModal')
# print(x[0].text)
for elem in x.contents:
    x=elem
    # print('-------\n\n',elem)

x=soup.select('#signupModal')
print(len(x))
for elem in x:
    x=elem
    # print(elem.text)

e=dom.xpath('/html/body/section/div/p[3]')
print(e[0].text)
# print(e)
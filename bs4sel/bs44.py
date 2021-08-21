from bs4 import BeautifulSoup
from lxml import etree,html
import requests

url="https://en.wikipedia.org/wiki/Taj_Mahal"
req=requests.get(url)
# print(req)

soup = BeautifulSoup(req.text, "html.parser")
# print(soup.prettify)

dom=etree.HTML(str(soup))
tree=html.fromstring(req.content)

# e=dom.xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[3]/ul/li[*]/a')
# # for i in range(len(e)):
# #     print(f"""https://en.wikipedia.org/wiki/Taj_Mahal#{e[i].get('href')}""")

x=dom.xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[7]/div[2]/div/ul/li[*]/div/div[2]/p')
# print(x)
for i in range(len(x)):
    g=x[i].text
    if len(g)>30:
        print(g,'\n')
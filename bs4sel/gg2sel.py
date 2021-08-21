from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome('/home/nisharg/Documents/Bash/bs4sel/chromedriver')

# driver.get('https://www.tuko.co.ke/339793-best-funny-jokes-a-girl-like.html')
driver.get('https://en.wikipedia.org/wiki/Taj_Mahal')

# ul1=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/section/section/article/div[1]/ul[1]')
# lis=ul1.find_elements_by_tag_name('li')
# print(lis)

ul=driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[3]/ul')
lis=ul.find_elements_by_tag_name('li')
for li in lis:
    print(li.text,'\n')
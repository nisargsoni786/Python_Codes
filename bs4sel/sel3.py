from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome('/home/nisharg/Documents/Bash/bs4sel/chromedriver')
driver.get('https://orteil.dashnet.org/cookieclicker/')

# actions=ActionChains(driver)

cookie=driver.find_element_by_id('bigCookie')
while(True):
    cookie.click()
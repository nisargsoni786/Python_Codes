from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome('/home/nisharg/Documents/Bash/bs4sel/chromedriver')
driver.get('https://www.techwithtim.net/')

link=driver.find_element_by_link_text('Python Programming')
link.click()

try:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Intermediate Python Tutorials"))
    )
    link.click()
    
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    link.click()
    driver.back()
    driver.back()
    driver.back()
except:
    print('ERROR')




# finally:
#     time.sleep(3)
#     driver.quit()
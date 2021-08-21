from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome('/home/nisharg/Documents/Bash/bs4sel/chromedriver')

driver.get('https://www.techwithtim.net/')
# print(driver.title)
# time.sleep(3)

searchbar=driver.find_element_by_xpath('//*[@id="search-2"]/form/label/input')
searchbar.send_keys('test')
searchbar.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)
    arts=main.find_elements_by_tag_name('article')
    for art in arts:
        header=art.find_element_by_class_name("entry-summary")
        print(header.text)
except:
        print('---------------------------------------------OOPS ERROR----------------------------------------')
finally:
    driver.quit()
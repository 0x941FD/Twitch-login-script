from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

my_token = "token"

driver = webdriver.Firefox()
driver.get("https://totp.danhersam.com/")
elem_ctoken = driver.find_element(By.CSS_SELECTOR,"input").clear()
elem_token = driver.find_element(By.CSS_SELECTOR,"input")
elem_token.send_keys(my_token + Keys.RETURN)
# In case it need some time to populate the content. 
# time.sleep(20)

html = driver.page_source
soup = BeautifulSoup(html)
logginTag = soup.find("a", {"id" : "token"})
print(logginTag)
driver.close()
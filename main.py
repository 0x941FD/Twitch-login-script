from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

my_username = "user"
my_password = "pass"

driver = webdriver.Firefox()
driver.get("http://www.twitch.tv/login")
elem_user = driver.find_element(By.ID,"login-username")
elem_passwd = driver.find_element(By.ID,"password-input")
elem_user.send_keys(my_username)
elem_passwd.send_keys(my_password + Keys.RETURN)
# In case it need some time to populate the content. 
time.sleep(20)

html = driver.page_source
soup = BeautifulSoup(html)
logginTag = soup.find("a", {"id" : "user_display_name"})
print(logginTag)
driver.close()
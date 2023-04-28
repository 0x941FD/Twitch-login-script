from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

accounts_file = open("Accounts/accounts.txt", "r")

line = 0
for line in accounts_file:
        my_username, my_password, my_token = line.replace("\n","").split(":")
        driver = webdriver.Firefox()
        driver.get("https://totp.danhersam.com/")
        elem_ctoken = driver.find_element(By.CSS_SELECTOR,"input").clear()
        elem_token = driver.find_element(By.CSS_SELECTOR,"input")
        elem_token.send_keys(my_token + Keys.RETURN)
        out = driver.find_element(By.ID,"token").text
        print(line+"\t 2FA: "+out)
        driver.close()
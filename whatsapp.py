"""
from selenium import webdriver
browser = webdriver.Chrome("/Users/yogesh/OneDrive/Desktop/whatsapp automation/chromedriver")
browser.get("https://www.selenium.dev/")
download = browser.find_element_by_link_text("Downloads")
download.click()
search = browser.find_element_by_id("gsc-i-id1")
search.send_keys("Downloads")
"""

#Whatsapp Code:

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("/Users/yogesh/OneDrive/Desktop/whatsapp automation/chromedriver")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser,600)

target = '"Yogesh Tekwani"'
string = "."
x_arg = '//span[contains(@title, ' + target +')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box = browser.find_element_by_class_name("_1Plpp")

for i in range(100):
	print(i)
	input_box.send_keys(string + Keys.ENTER)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s=Service("C:/Program Files/Google/Chrome/Application/chrome.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.instagram.com")
username=driver.find_element_by_xpath('''//*[@id="loginForm"]/div/div[1]/div/label/input''')
username.send.keys("_sujal_gopani__")
password=driver.find_element_by_xpath('''//*[@id="loginForm"]/div/div[2]/div/label/input''')
password.send.keys("gopanigopani@123")
password.send.keys(Keys.ENTER)

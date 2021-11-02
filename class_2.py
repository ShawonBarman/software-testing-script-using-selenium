from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
dr = webdriver.Chrome(executable_path="F:\\Python program\\web drivers\\chromedriver.exe")  #where your chrome webdriver

dr.get("https://www.google.com/")
print(dr.current_url)
print(dr.title)

time.sleep(2)

dr.maximize_window()

dr.find_element_by_name("q").send_keys("University of Asia Pacific")
time.sleep(3)

dr.find_element_by_name("btnK").send_keys(Keys.ENTER)

time.sleep(3)

dr.close()
print("Simple test case successfully")
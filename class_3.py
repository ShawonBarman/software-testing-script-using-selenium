from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
dr = webdriver.Chrome(executable_path="F:\Python program\web drivers\chromedriver.exe")   #where your chrome webdriver
dr.get("https://opensource-demo.orangehrmlive.com/")
print(dr.current_url)
print(dr.title)

time.sleep(2)

dr.find_element_by_name("txtUsername").send_keys("Admin")
time.sleep(2)
dr.find_element_by_name("txtPassword").send_keys("admin123")
time.sleep(2)
dr.find_element_by_name("Submit").click()
time.sleep(2)
print("Button clicked")
dr.close()
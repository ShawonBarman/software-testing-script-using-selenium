from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
dr = webdriver.Chrome(executable_path="F:\Python program\web drivers\chromedriver.exe")   #where your chrome webdriver
dr.get("http://127.0.0.1:8000/")
print(dr.current_url)
print(dr.title)
time.sleep(2)

dr.find_element(By.XPATH,"//a[contains(text(),'Signin')]").click()
print("clicked signin link and perfectly go to signin page")
time.sleep(2)

dr.find_element_by_name("username").send_keys("Shawon43")
print("Username writted")
time.sleep(2)

dr.find_element_by_name("password").send_keys("uapcse12")
print("Password writted")
time.sleep(2)

dr.find_element(By.XPATH,"//button[contains(text(),'Signin')]").click()
print("clicked signin button and perfectly signin account and go to home page")
time.sleep(2)

dr.find_element(By.XPATH,"//a[contains(text(),'Log out')]").click()
print("clicked log out link and perfectly logout account")
time.sleep(2)

print("End testing program")
dr.close()
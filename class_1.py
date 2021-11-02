from selenium import  webdriver
import time
dr = webdriver.Chrome(executable_path="F:\Python program\web drivers\chromedriver.exe")  #where your chrome webdriver

dr.get("https://uap-bd.edu/")
print(dr.current_url)
print(dr.title)
time.sleep(3)

dr.get("https://cse.uap-bd.edu/")
print(dr.current_url)
print(dr.title)
time.sleep(3)

dr.back()
print(dr.current_url)
print(dr.title)
time.sleep(3)

dr.forward()
print(dr.current_url)
print(dr.title)
time.sleep(5)

dr.close()
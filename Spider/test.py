# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import os




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/Usr/bin/ChromeDriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)


url = r'http://got.goermicro.com:8089/got/temperature/attend.html'
driver.get(url)

print("访问页面成功")

username = driver.find_element(by='id', value='employeeNumber')
StudentID = '9002370'
username.send_keys(StudentID)

print("填报员工号成功")

secretKey = driver.find_element(by='id', value='numId')
KeyNum = '041815'
secretKey.send_keys(KeyNum)

print("填报身份证成功")

logbtn = driver.find_element(by='id', value='sub')
logbtn.click()

print("提交员工信息成功")
time.sleep(1)

logbtn = driver.find_element(by='id', value='agreement')
logbtn.click()

print("同意协议")


time.sleep(1)


driver.get('http://got.goermicro.com:8089/got/temperature/to_temperature.html')

print("进入体温填报页面成功")
print(driver.title)

time.sleep(50)




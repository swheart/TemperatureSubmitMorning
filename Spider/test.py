# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def submit():
    try:
        driver = webdriver.Chrome(executable_path='/Usr/local/bin/ChromeDriver')
        print("填报失败1")

        url = r'http://got.goermicro.com:8089/got/temperature/attend.html'
        driver.get(url)
        print("填报失败2")

        username = driver.find_element(by='id', value='employeeNumber')
        StudentID = '9002370'
        username.send_keys(StudentID)
        print("填报失败3")


        secretKey = driver.find_element(by='id', value='numId')
        KeyNum = '041815'
        secretKey.send_keys(KeyNum)
        print("填报失败4")

        logbtn = driver.find_element(by='id', value='sub')
        logbtn.click()
        print("填报失败5")

        time.sleep(1)

        logbtn = driver.find_element(by='id', value='agreement')
        logbtn.click()
        print("填报失败6")

        time.sleep(1)


        driver.get('http://got.goermicro.com:8089/got/temperature/to_temperature.html')

        print(driver.title)

        time.sleep(50)



    except Exception as e:
        print("填报失败")
        pass


if __name__ == '__main__':
    submit()


# -*- coding:utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def submit():
    try:
        driver = webdriver.Chrome(executable_path='/Usr/local/bin/ChromeDriver')

        url = r'http://got.goermicro.com:8089/got/temperature/attend.html'
        driver.get(url)

        username = driver.find_element(by='id', value='employeeNumber')
        StudentID = '9002370'
        username.send_keys(StudentID)

        secretKey = driver.find_element(by='id', value='numId')
        KeyNum = '041815'
        secretKey.send_keys(KeyNum)

        logbtn = driver.find_element(by='id', value='sub')
        logbtn.click()

        time.sleep(1)

        logbtn = driver.find_element(by='id', value='agreement')
        logbtn.click()


        time.sleep(1)


        driver.get('http://got.goermicro.com:8089/got/temperature/to_temperature.html')


        time.sleep(50)



    except Exception as e:
        alert("填报失败")
        pass


if __name__ == '__main__':
    submit()


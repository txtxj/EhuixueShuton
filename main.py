from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime

# time for user to enter password (second)
wait_time = 10

# time for driver to load pages (second)
req_timeout = 4

# time gap between two search (second)
query_gap = 1

driver = webdriver.Chrome()
driver.implicitly_wait(req_timeout)
driver.maximize_window()

# your phone number, password, lessonId
username = ""
password = ""
lessonId = ""


def login():
    driver.get("http://www.ehuixue.cn/index/login/login.html")
    driver.implicitly_wait(req_timeout)
    driver.find_element(By.NAME, "account").send_keys(username)
    driver.find_element(By.NAME, "pwd").send_keys(password)
    time.sleep(wait_time)
    driver.execute_script("saveinfo()")
    time.sleep(req_timeout)
    driver.get("http://www.ehuixue.cn/index/study/inclass.html?cid=" + lessonId)


def start_watch():
    while True:
        driver.find_element(By.CLASS_NAME, "cview").click()
        time.sleep(query_gap)
        try:
            nxt = driver.find_element(By.CLASS_NAME, "layui-btn.layui-btn-normal.layui-btn-xs")
            nxt.click()
        except:
            print("No 'next' button!")


login()
start_watch()

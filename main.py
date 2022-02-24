from selenium import webdriver
from selenium.webdriver.common.by import By

import time

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
    driver.get("http://www.ehuixue.cn/")
    driver.implicitly_wait(req_timeout)
    driver.get("http://www.ehuixue.cn/index/login/login.html")
    driver.implicitly_wait(req_timeout)
    driver.find_element(By.NAME, "account").send_keys(username)
    driver.find_element(By.NAME, "pwd").send_keys(password)
    time.sleep(wait_time)
    driver.execute_script("saveinfo()")
    time.sleep(req_timeout)
    # if you use https, you have to use flash player
    driver.get("http://www.ehuixue.cn/index/study/inclass.html?cid=" + lessonId)


def start_watch():
    while True:
        driver.find_element(By.CLASS_NAME, "cview").click()
        driver.implicitly_wait(req_timeout)
        try:
            nxt = driver.find_element(By.CLASS_NAME, "layui-btn.layui-btn-normal.layui-btn-xs")
            nxt.click()
        except:
            print("No 'next' button!")


login()
start_watch()

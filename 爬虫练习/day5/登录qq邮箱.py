# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
driver.switch_to.frame("login_frame") # 这里是iframe的id
driver.find_element_by_id("switcher_plogin").click()
driver.find_element_by_id("u").send_keys("***@qq.com")
driver.find_element_by_id("p").send_keys("***")
driver.find_element_by_id("login_button").click()
time.sleep(10)
driver.quit()

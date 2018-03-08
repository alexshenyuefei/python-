from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://accounts.douban.com/login')
driver.find_element_by_id('email').send_keys('shenweiyi1994@126.com')
driver.find_element_by_id('password').send_keys('dlxy1994')
print(driver.page_source)
time.sleep(5)
#验证码待优化
driver.find_elements_by_xpath("//input[@value='登录']")[0].click()


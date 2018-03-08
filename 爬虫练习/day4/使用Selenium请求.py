from selenium import webdriver


driver = webdriver.Chrome()  #调用chrome浏览器
driver.get('https://www.baidu.com')
print(driver.title)
driver.find_element_by_id('kw').send_keys('阿瓦隆')
driver.find_element_by_id("su").click()


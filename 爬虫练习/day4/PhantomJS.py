from selenium import webdriver


driver = webdriver.PhantomJS(r'C:\phantomjs\bin\phantomjs.exe')
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com/")
driver.get("https://uniqlo.tmall.com/category-97377015.htm")
driver.save_screenshot("优衣库截屏.png")

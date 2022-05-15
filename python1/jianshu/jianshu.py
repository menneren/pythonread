import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#导入 webdriver
driver=webdriver.Firefox()
#打开 firefox 浏览器
driver.get('http://www.jianshu.com')
#打开 LMD 后台登陆页面
driver.maximize_window()

#搜索框输入元素
element = driver.find_element(By.ID, "q")
element = driver.find_element(By.PLACEHOLDER, "搜索")
#<input type="text" name="q" id="q" value="" autocomplete="off" placeholder="搜索" class="search-input" data-mounted="1">

#输入字符串，在这个输入框里
element.send_keys('黑羽\n')







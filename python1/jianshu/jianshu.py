import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

#导入 webdriver
driver = webdriver.Firefox()
#打开 firefox 浏览器
driver.get('https://www.jianshu.com/')
#打开 LMD 后台登陆页面
driver.maximize_window()

'''
#搜索框输入元素
try:
    element = driver.find_element(By.ID, "sign_in")
    element.click()
except NoSuchElementException:
    print("不存在")

#<input type="text" name="q" id="q" value="" autocomplete="off" placeholder="搜索" class="search-input" data-mounted="1">

#输入字符串，在这个输入框里
#element.send_keys('黑羽\n')


#输入手机号或邮箱
phone = driver.find_element(By.ID, "session_email_or_mobile_number")
phone.send_keys('15926436854')
#输入秘密
password = driver.find_element(By.ID, "session_password")
password.send_keys('liujiyang91')
#点击登陆
driver.find_element(By.ID, "sign-in-form-submit-btn").click()

#输入验证码
driver.find_element(By.ID, "session_code").send_keys('653168\n')
'''

#class属性
#/p/ce7701b6db34
element = driver.find_element(By.CLASS_NAME, "title")
element.click()
print(element)

#获取属性
print(element.get_attribute('path'))

'''
titles = driver.find_element(By.TAG_NAME, 'title')
for title in titles:
    print(title.text)
'''

'''
#第一个元素，等待输出
while True:
    try:
        element = driver.find_element(By.CLASS_NAME, '1')
        print(element.text)
        break
    except:
        time.sleep(1)
'''


'''
#find_element符合条件的第一个元素
#find_elements符合条件的所有元素
#元素在界面的内容，列表
for element in elements:
    print(element.text)
'''
#driver.find_element_by_tag_name('span')标签名

#为定位到元素
#driver.find_element(By.XPATH, "d").click()


#隐士等待
#driver.implicitly_wait(5)    #每隔半秒找一次，一直等待5秒




time.sleep(2)

driver.quit()




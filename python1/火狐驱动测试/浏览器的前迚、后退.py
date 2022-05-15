#显式等待
#显式等待使WebdDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）。
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
#窗口最大化
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.ID,"email")))
#显示等待，等待邮箱输入框
driver.find_element(By.ID, "email").send_keys('lib@163.com')
#输入用户名
driver.find_element(By.ID, "password").send_keys('12345678')
#输入密码
driver.find_element(By.CSS_SELECTOR, "button.btn").click()
#点击登陆
driver.implicitly_wait(3)
#隐式等待 3 秒
driver.find_element(By.CSS_SELECTOR, '#dashboard-menu >li:nth-child(2) > a:nth-child(1)').click()
#点击待审核创意
driver.find_element(By.CSS_SELECTOR, 'select.span1:nthchild(8)').click()
#点击审核状态的下拉框
driver.back()
#后退
driver.forword()
#前进
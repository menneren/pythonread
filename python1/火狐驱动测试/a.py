from selenium import webdriver
import time
# 启动浏览器
driver = webdriver.Firefox()

# 访问一个网页
driver.get("https://www.baidu.com")

# 退出访问或者会话 杀掉进程 不占用资源
driver.quit()

# 关闭当前窗口 没有杀掉进程 没有退出浏览器进程
driver.close()



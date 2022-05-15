from selenium import webdriver
import time
# 启动浏览器
driver = webdriver.Firefox()
# 访问一个网页
driver.get("https://www.baidu.com")
# 窗口最大化
driver.maximize_window()
# 访问另一个网页
driver.get("http://www.taobao.com")
# 退回上一页
driver.back()
time.sleep(1) # 强制等待1S
driver.implicitly_wait(5)  # 隐形等待5S，如果等到了进程马上运行，如没有等到，5秒后报错
# 退回下一页
driver.forward()
# 刷新
driver.refresh()
# 获取标题
print(driver.title)
# 获取网址
print(driver.current_url)
# 窗口的ID
print(driver.current_window_handle)



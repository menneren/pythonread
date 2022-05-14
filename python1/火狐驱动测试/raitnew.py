from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.baidu.com")

time.sleep(5)

driver.find_element(By.ID,"kw").click()
driver.find_element(By.ID,"kw").send_keys("python")
time.sleep(2)
driver.quit()



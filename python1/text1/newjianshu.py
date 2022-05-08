import webbrowser
webbrowser.open('https://www.jianshu.com')

import time
import pyautogui

x, y= 302, 534 #鼠标需要移动到的位置

num_seconds = 2 #将鼠标移动到指定坐标的间隔时间

time.sleep(8) #延迟8秒

pyautogui.moveTo(x, y, duration=num_seconds)

time.sleep(3) #延迟3秒

i = 60

whele:
    i-= 1
    time.sleep(5)

pyautogui.click()








import time
import pyautogui
#pyautogui库安装问题
import pyautogui

#pip install pyautogui    #安装库

def click_operation():
    """点击操作"""
    for i in range(1):

        #鼠标需要移动到的位置
        x, y = 1396, 850

        #将鼠标移动到指定坐标的间隔时间
        num_seconds = 2

        #延迟2秒
        time.sleep(2)

        #duration 鼠标移动时间
        #pyautogui.move(x,y,duration=num_seconds)
        #将鼠标移动到指定位置
        pyautogui.moveTo(x, y)

        #点击
        pyautogui.click()

        #鼠标需要移动到的位置
        x, y = 1900, 15

        #延迟2秒
        time.sleep(2)

        #将鼠标移动到指定位置
        pyautogui.moveTo(x, y)

        #延迟8秒
        time.sleep(10)

        #点击
        pyautogui.click()


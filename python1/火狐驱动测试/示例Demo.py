# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 15:03
# @Author  : CuiShuangqi
# @File    : selenium_ActionChains.py
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

class TestSeleniumActionChains(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(3)

    def tearDown(self) -> None:
        sleep(5)
        self.driver.quit()

    # 鼠标悬浮在元素上
    def test_001(self):
        #  百度首页右上角"设置"按钮
        print("鼠标悬浮在元素上")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()

    # 鼠标左键单击元素
    def test_002(self):
        #  百度首页右上角"设置"按钮
        print("鼠标左键单击元素")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.click(ele).perform()

    # 鼠标左键单击元素不松开
    def test_003(self):
        #  百度首页右上角"设置"按钮
        print("鼠标左键单击元素不松开")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.click_and_hold(ele).perform()

    # 鼠标左键双击元素
    def test_004(self):
        #  百度首页右上角"设置"按钮
        print("鼠标左键双击元素")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.double_click(ele).perform()

    # 鼠标右键单击元素
    def test_005(self):
        #  百度首页右上角"设置"按钮
        print("鼠标右键单击元素")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.context_click(ele).perform()

    # 鼠标左键拖拽某个元素至某个元素松开
    def test_006(self):
        #  百度首页右上角"设置"按钮
        print("鼠标左键拖拽某个元素松开")
        # 源位置
        ele_source = self.driver.find_element_by_xpath("//*[@id='hotsearch-content-wrapper']/li[1]/a/span[1]")
        # 目标位置
        ele_target = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_source, ele_target).perform()


if __name__ == '__main__':
    unittest.main()

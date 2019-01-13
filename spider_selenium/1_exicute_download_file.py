# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 创建Options对象
options = Options()
options.set_headless()
# options.add_argument('--headless')
# 创建Chrome 的驱动对象,如果是Windows()中传入driver的路径: “c:…/pantomjs.exe”
Chr_driver = webdriver.Chrome("C:\\MyFile\\Downloads\\chromedriver.exe",options=options)

# 加载页面 “https://www.baidu.com”
Chr_driver.get("https://www.baidu.com")
# 保存当前界面
Chr_driver.save_screenshot("baidu.png")

# 关闭当前窗口
Chr_driver.close()
# 退出浏览器
Chr_driver.quit()

# 流程：
# 1、导入模块
# 2、创建Chrome的webdriver对象、[和创建Options对象]
# 3、发送请求
# 4、对元素定位并进行操作
# [5、查看请求信息]
# [ 6、对请求信息进行操作]
# 退出：关闭选项卡、退出浏览器 --- finally必须要退出，否则容易造成内存泄漏

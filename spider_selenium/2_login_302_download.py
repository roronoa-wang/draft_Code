# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# 流程：
# 1、导入模块
# 2、创建Chrome的webdriver对象、[和创建Options对象]
# 3、发送请求
# 4、对元素定位并进行操作
# [5、查看请求信息]
# [ 6、对请求信息进行操作]
# 退出：关闭选项卡、退出浏览器 --- finally必须要退出，否则容易造成内存泄漏

class BaiduSpider():
    def __init__(self):
        # 创建Options对象
        options = Options()
        options.set_headless()
        # options.add_argument('--headless')
        # 创建Chrome 的驱动对象,如果是Windows()中传入driver的路径: “c:…/pantomjs.exe”
        self.Chr_driver = webdriver.Chrome("C:\\MyFile\\Downloads\\chromedriver.exe")

    def __del__(self):
        print "关闭浏览器了"
        self.Chr_driver.quit()

    def run(self):
        # 加载页面 “https://www.baidu.com”
        self.Chr_driver.get("https://www.baidu.com")
        # print a
        # 保存当前界面
        self.Chr_driver.save_screenshot("baidu.png")

if __name__ == '__main__':
    bd = BaiduSpider()
    try:
        bd.run()
    except Exception as e:
        print e
    finally:
        print "关闭了浏览器驱动"
        del bd









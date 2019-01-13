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

# 加上等待响应时间

class BaiduSpider():
    def __init__(self):
        # 创建Options对象
        options = Options()
        options.set_headless()
        # options.add_argument('--headless')
        # 创建Chrome 的驱动对象,如果是Windows()中传入driver的路径: “c:…/pantomjs.exe”
        self.Chr_driver = webdriver.Chrome("C:\\MyFile\\Downloads\\chromedriver.exe", options=options)
        self.user = ""
        self.pw = ""

    def __del__(self):
        print "关闭浏览器了"
        self.Chr_driver.close()  # 关闭当前标签页
        self.Chr_driver.quit()

    def run(self):
        """
        1、登录--账号密码
        2、重定向302：
            方式1：Chr_driver.get当前 窗口切换，
            方式2:打开新的标签页，然后切换句柄 再 请求新的URL
        3、输入点击下载，打开新page
        4、操作新page --- 点击下载
        其他问题：等待网站响应、隐式等待
        打开一个标签页就记住它的句柄
        :return: 
        """

        # 1、登录--账号密码
        self.Chr_driver.get("http://gufenso.huizhanzhang.com/index.php")
        handle1 = self.Chr_driver.current_window_handle
        print "当前窗口句柄：", handle1
        time.sleep(2)

        # 2、重定向302：
        # 方式1：
        # self.Chr_driver.get("https://www.baidu.com/")
        # handle1 = self.Chr_driver.current_window_handle
        # print "当前窗口句柄：", handle1
        # time.sleep(2)

        # 方式2：
        js = "window.open('https://www.baidu.com/')"
        self.Chr_driver.execute_script(js)

        handles_2 = self.Chr_driver.window_handles
        # print handles, ": ", type(handles)
        # 切换标签页：方式1--使用键盘快捷键，方式2---使用id准确切换
        for h in handles_2:
            print h
            # if h != handle1:
            if h != handle1:
                self.Chr_driver.switch_to_window(h)
                print "切换到: ", h

        handle2 = self.Chr_driver.current_window_handle
        print "当前窗口句柄handle2：", handle2
        time.sleep(2)

        kw = self.Chr_driver.find_element_by_id("kw")
        print "文本框标签：", kw.tag_name
        kw.send_keys("gitee")
        time.sleep(1)

        bd_click = self.Chr_driver.find_element_by_id("su")
        print "搜索标签：", bd_click.tag_name, "\n\n"
        bd_click.click()
        time.sleep(1)

        handle = self.Chr_driver.current_window_handle
        print "当前窗口句柄：", handle

        gitee_page = self.Chr_driver.find_element_by_xpath('//*[@id="1"]/h3')
        print "gitee_page的标签：", gitee_page.tag_name, "\n\n"
        gitee_page.click()
        time.sleep(1)


        # 4
        handles_2 = self.Chr_driver.window_handles
        # print handles, ": ", type(handles)
        # 切换标签页：方式1--使用键盘快捷键，方式2---使用id准确切换
        for h in handles_2:
            print h
            # if h != handle1:
            if h != handle1 and h != handle2:
                self.Chr_driver.switch_to_window(h)
                print "切换到: ", h

        # self.Chr_driver.close()

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









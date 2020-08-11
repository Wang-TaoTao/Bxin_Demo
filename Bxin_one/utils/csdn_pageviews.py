import random
import sys

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 刷csdn文章点击量
class Csdn(object):

    def __init__(self):
        self.opts = Options()
        self.opts.headless = True  # 设置无头模式，相当于执行了opt.add_argument('--headless')和opt.add_argument('--disable-gpu')(--disable-gpu禁用gpu加速仅windows系统下执行)。
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        self.opts.add_experimental_option('prefs', prefs) # 不加载图片
        self.chrome_driver = '/Users/bixin/Downloads/chromedriver'
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver, options=self.opts)

    def request_csdn(self, url):

        print("开始请求:{0}".format(url))
        self.driver.get(url)


    def click_paga_article(self):
        res = self.driver.find_elements_by_xpath('//*[@id="mainBox"]/main/div/div')

        self.driver.implicitly_wait(10)

        for re in res:
            re.click()

            # 限制点击时间
            time.sleep(random.randint(1,3))
        # 关闭当前所有窗口
        self.driver.quit()


    # def swith_window(self):
    #     # 切换句柄
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #
    #     # 拉到页面下方
    #     js = 'scrollTo(0,10000000)'
    #     self.driver.execute_script(js)
    #
    #     self.driver.implicitly_wait(10)

    def flip(self, url, i, page):

        if i > page:
            flag = True
            return flag

        next_url = '{0}/article/list/{1}'.format(url, i)

        self.driver.get(next_url)



if __name__ == '__main__':

    # 请求的csdn博客地址
    url = 'https://blog.csdn.net/WangTaoTao_'
    # 博客共有多少页
    page = 3

    # 实例化
    csdn = Csdn()
    # 发起请求
    csdn.request_csdn(url)
    i=2
    # 无限点击
    while True:
        # 点击某一页文章
        csdn.click_paga_article()
        # 关闭当前所有窗口
        csdn.driver.quit()
        # 下一页
        flag = csdn.flip(url, i, page)
        i += 1
        if flag:
            # 限制访问时间
            time.sleep(random.randint(66,88))
            csdn.request_csdn(url)
            i = 2
            flag = False












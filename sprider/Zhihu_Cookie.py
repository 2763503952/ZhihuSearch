from DrissionPage import ChromiumPage,ChromiumOptions,Chromium
from DrissionPage.errors import BrowserConnectError
from settings.setting import CHROME_PATH, COOKIE_URL
import time
class PageZhihu:
    def __init__(self):
        self.options = ChromiumOptions().auto_port() # 以无头模式启动
        self.tab: Chromium = Chromium(addr_or_opts=self.options)
        self.is_chrome()
        self.url = COOKIE_URL

    def get_cookie(self):
        """
        返回字符串形式的cookie和dc_0参数
        :return: 返回{cookie, dc_0}
        """
        tab = self.tab.latest_tab
        tab.get(self.url)
        while True:
            # 判断cookie中是否有['SESSIONID', 'd_c0', 'JOID'], 如果没有就等待DOM更新
            cookie_count = 0
            for cookie in tab.cookies():
                if cookie['name'] in ['SESSIONID', 'd_c0', 'JOID']:
                    cookie_count = cookie_count + 1
            if cookie_count == 3:
                break
            time.sleep(1)   # 等待一秒
        cookie_str = ''
        cookie_dc0 = ''
        for cookie in tab.cookies():
            cookie_str = cookie_str + cookie['name'] + '=' + cookie['value'] + '; '
            if cookie.get('name')  == 'd_c0':
                cookie_dc0 = cookie.get('value')
        self.close(tab) # 关闭浏览器
        return {
            'cookie': cookie_str[:-2],
            'dc_0': cookie_dc0
        }

    def close(self, tab):
        tab.close()


    def is_chrome(self):
        """
        验证chrome是否可用
        """
        try:
            tab = self.tab.latest_tab
            tab.get('https://DrissionPage.cn')
        except BrowserConnectError as e:
            print(f"{str(e)}，请手动在配置中填写本机谷歌浏览器安装地址")
            self.options.set_browser_path(CHROME_PATH).save()




if __name__ == '__main__':
    print(PageZhihu().get_cookie())
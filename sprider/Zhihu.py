import execjs
import requests
from sprider.Zhihu_Cookie import PageZhihu
import hashlib
from settings.setting import JS_PATH
class SearchZhihu:
    def __init__(self, keyword: str):
        self.keyword: str = keyword
        self.url: str = 'https://www.zhihu.com/'
        self.cookie_json: dict = self.get_cookie
        self.cookie: str = self.cookie_json['cookie']


    def search(self):
        dc_0 = self.cookie_json['dc_0']
        x_96 = self.parse_x96(dc_0)
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cookie": self.cookie,
            "priority": "u=1, i",
            "referer": f"https://www.zhihu.com/search?q={self.keyword}&type=people",
            "sec-ch-ua": "\\Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\\Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "x-api-version": "3.0.91",
            "x-app-za": "OS=Web",
            "x-requested-with": "fetch",
            "x-zse-93": "101_3_3.0",
            "x-zse-96": '2.0_'+x_96,  # 需要被逆向的数据
        }
        params = {
            "gk_version": "gz-gaokao",
            "t": "people",
            "q": self.keyword,
            "correction": "1",
            "offset": "0",
            "limit": "20",
            "filter_fields": "",
            "lc_idx": "0",
            "show_all_topics": "0",
            "search_source": "Normal"
        }
        url = self.url + 'api/v4/search_v3'
        response = requests.get(url, headers=headers, params=params)
        return response

    def get_md5(self, dc0: str):
        text = f"101_3_3.0+/api/v4/search_v3?gk_version=gz-gaokao&t=people&q={self.keyword}&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal+{dc0}"
        md5_hash = hashlib.md5()
        # 更新hash对象以添加需要加密的字符串，注意需要将字符串编码为字节
        md5_hash.update(text.encode('utf-8'))
        # 获取加密后的16进制表示的字符串
        encrypted_text = md5_hash.hexdigest()
        # print("text=",text)
        return encrypted_text
    @property
    def get_cookie(self):
        return PageZhihu().get_cookie()

    def parse_x96(self, dc0: str):
        # 读取JavaScript文件的内容
        with open(JS_PATH, 'r', encoding='utf-8') as f:
            js_code = f.read()
        # 编译JavaScript代码
        ctx = execjs.compile(js_code)
        md5 = self.get_md5(dc0)
        # 调用JavaScript函数并获取结果
        result = ctx.call("res",md5,)
        return result


if __name__ == '__main__':
    SearchZhihu('wud').search()
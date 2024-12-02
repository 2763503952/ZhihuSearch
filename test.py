import hashlib
import time


def test_md5():
    text = '101_3_3.0+/api/v4/search_v3?gk_version=gz-gaokao&t=people&q=wud&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal+AGDSRG91oRmPTrlU0ROHVwXXXy0wU0b5T5g=|1733112041'
    md5_hash = hashlib.md5()
    # 更新hash对象以添加需要加密的字符串，注意需要将字符串编码为字节
    md5_hash.update(text.encode('utf-8'))
    # 获取加密后的16进制表示的字符串
    encrypted_text = md5_hash.hexdigest()
    print(encrypted_text)


def test_request():
    import requests

    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cookie": "_zap=462065d8-20d7-495e-8b93-0a4e538d36e4; _xsrf=a15c7444-ab38-4a2a-9a18-951246013f8b; d_c0=AGDSRG91oRmPTrlU0ROHVwXXXy0wU0b5T5g=|1733112041; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1733112047; HMACCOUNT=AA08B1D738E4DB1D; SESSIONID=q6mPrc2vReUEuxJVol7tdBoXU6KVJrBP7xLHDPzB4af; JOID=WloRAUrHNTdIGP_0Ls0GaZ1ygFY7vAVcG2OWwF6cWmQLbo60fiEFfyUb8_Qr2ngUVKFaxCEeDQ52lkBdMEcbLnE=; osd=WlERA0LHPjdKEP__Ls8OaZZygl47twVeE2OdwFyUWm8LbIa0dSEHdyUQ8_Yj2nMUVqlazyEcBQ59lkJVMEwbLHk=; __snaker__id=MRyh7s35tPOx9V7x; __zse_ck=003_b7lZJc3/sQlXy5sFvc5BiVCJD5WA8L1+SjMvHRKqztwg=A06PHaap2TajH/OtYMXbqsQDTYeLq=lsJ=Fz==uWd17XNs0o7PVslHHNSmPtKTJ; captcha_session_v2=2|1:0|10:1733127980|18:captcha_session_v2|88:S3locHlrYkErdEVtV3VpbTZBcjJia0FGQnU1RE9DMDJvUTAzaUJENFN3eHorVC9EWmtON0pPVEw0RUtnU3FVMQ==|077b939426e5572e9fe0c9cdb92edb62e7aef28c5ef271d46a7c116cdce45ee4; gdxidpyhxdE=mV4%5CqiAdk0rWhw7xRsoEons%5CHMzEgUSxubg2ZMaDG19WhtM1JR62QXKWqLuJ%2BySxWjOZqeCXbxtd1udp2LsUqd7nu6WWQKPIqAHhN%2Fz6m8z0YSzlGiu3%2BSlCrknbzA4lA4I0DV5gOfHoh3ylA8mRSCdV0lA8b5VOLJawi0U4%2BSww%5CR1G%3A1733129498716; o_act=login; ref_source=search; z_c0=2|1:0|10:1733129127|4:z_c0|92:Mi4xb0FUY0NnQUFBQUFBWU5KRWIzV2hHU1lBQUFCZ0FsVk5wc0U2YUFBeVZaVDZoUG1zQUxQVldfeExDR04ycXAySkpB|a98b6bab7ff57b1d36416c74fb67c97547af2cfde74ca5b67ddafa739cc1f246; BEC=4589376d83fd47c9203681b16177ae43; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1733132692",
        "priority": "u=1, i",
        "referer": "https://www.zhihu.com/search?q=wud&type=people",
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
        "x-zse-96": "2.0_09ocBJ+h0NJqDUwZ6kijrj7Z+eY=RddXOPPCv2Io8of9HCpoGPHHduPqUV3+0guy"
    }
    url = "https://www.zhihu.com/api/v4/search_v3"
    params = {
        "gk_version": "gz-gaokao",
        "t": "people",
        "q": "wud",
        "correction": "1",
        "offset": "0",
        "limit": "20",
        "filter_fields": "",
        "lc_idx": "0",
        "show_all_topics": "0",
        "search_source": "Normal"
    }
    response = requests.get(url, headers=headers, params=params)

    print(response.text)
    print(response)

test_request()
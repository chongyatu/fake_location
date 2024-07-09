import requests as req
from bs4 import BeautifulSoup
import os
token = os.getenv("TOKEN", "")

if not token:
    print("请配置TOKEN环境变量")
    exit(-1)
urls = [
    "http://k8n.cn/student/course/90621/punchs",
    "http://k8n.cn"
]
headers = {
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    "Cookie": token
}
response = req.get(urls[0], headers=headers)
if response.text:
    bs = BeautifulSoup(response.text, "html.parser")
    forms = bs.find_all("form")
    if forms:
        for f in forms:
            url = urls[1] + f.get("action")
            print(url)
            body = {'id': url[url.rfind('/') + 1:],
                    'lat': 26.0573213,
                    'lng': 119.1952560,
                    'acc': 30,
                    'res': "",
                    "gps_addr": ""}
            # print(body)
            res = req.post(url, body, headers=headers)
            print(res.text)
    else:
        print("没有开启签到通知!!")
import re
import requests
import random
import time

"""
针对小说屋 https://maoyan.com/board/4 的爬虫
1.访问10页
2.解析top前100电影排行的排名，封面图片，电影名，主演，上映时间，评分，生成josn格式保存到top中
注意：本网页存在滑动验证跳转方式的反爬

"""


class maoyan():
    def __init__(self, number):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.149 Safari/537.36"}
        self.url = 'https://maoyan.com/board/4'
        self.number = number

    def req(self, url):
        try:
            r = requests.get(url=url, headers=self.headers)
            if r.status_code == 200:
                r.encoding = r.apparent_encoding
                time.sleep(random.randint(1, 10))
                return r.text
            else:
                return None
        except ConnectionError as e:
            print(e)

    def parse(self, html, top):
        data = re.findall(
            r'<dd.*?board-index.*?>(.*?)<.*?<img data-src="(.+?)".*?name.*?}">(.+?)</a.*?star">(.+?)</p.*?releasetime">(.+?)</p.*?integer">(.+?)</i.*?fraction">(.+?)</i>',
            html, re.S)
        for data in data:
            c = {
                "Ranking": data[0],
                "jpg": data[1],
                "name": data[2],
                "actor": data[3].strip(),
                "release time": data[4],
                "score": data[5] + data[6]
            }
            top.append(c)

    def save(self, top):
        for top in top:
            print(top)

    def start(self):
        top = []
        for i in range(self.number // 10):
            a = self.req(self.url + f'?offset={i * 10}')
            self.parse(a, top)
        self.save(top)


def main():
    mayan = maoyan(100)
    mayan.start()


if __name__ == '__main__':
    main()

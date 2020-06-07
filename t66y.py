import requests
from requests_html import HTMLSession
import re

proxies = {"http": "http://127.0.0.1:63632", "https": "http://127.0.0.1:63632"}
list_url = 'http://t66y.com/thread0806.php?fid=8&type=1'
page_url = 'http://t66y.com/htm_data/8/1811/3345760.html'
base_url = 'http://t66y.com/'


def f1():
    html = requests.get(list_url, proxies=proxies)
    html.encoding = 'gbk'

    title = re.findall('<a href="htm_data.*html"', html.text, re.S)
    for each in title:
        print(each)


def f2():
    session = HTMLSession()
    r = session.get(list_url, proxies=proxies)
    r.encoding = 'gbk'

    for l in r.html.links:
        if re.match(r'htm_data/', l):
            full_url = base_url + l

            session2 = HTMLSession()
            r2 = session2.get(full_url, proxies=proxies)
            r2.encoding = 'gbk'

            for l2 in r2.html.links:
                # if re.match(r'http.*jpg', l2):
                print(l2)


def f3():
    session = HTMLSession()
    r = session.get(page_url, proxies=proxies)
    r.encoding = 'gbk'

    print(r.text)


def f4():
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(page_url, proxies=proxies, headers=headers)
    r.encoding = 'gbk'
    print(r.text)


if __name__ == '__main__':
    f4()

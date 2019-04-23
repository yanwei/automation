from requests_html import HTMLSession
import pandas as pd
import time


xclient_info_hot_page = 'https://xclient.info/hot'


def check_version(url):
    session = HTMLSession()
    r = session.get(url)
    r.encoding = 'utf-8'
    current_ver = r.html.xpath(
        '//*[@id="body"]/div/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td', first=True).text
    update_date = r.html.xpath(
        '//*[@id="body"]/div/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td', first=True).text
    return current_ver, update_date


def check_hot_page():
    session = HTMLSession()
    r = session.get(xclient_info_hot_page)
    r.encoding = 'utf-8'
    software_list = r.html.xpath('//*[@id="body"]/div[1]/div/div/ul/li/div/a')

    ver_info = []
    count = 0
    for software in software_list:
        title = software.attrs['title']
        url = software.attrs['href']
        ver, date = check_version(url)
        record = {'title': title, 'date': date, 'ver': ver, 'url': url}
        print(record)
        ver_info.append(record)
        time.sleep(0.1)
        count += 1
        # print('*', end='')
        # if count > 3:
        #     break

    print('')
    df = pd.DataFrame(ver_info)
    print(df.sort_values(by='date', ascending=False)[['date', 'title']])


if __name__ == "__main__":
    check_hot_page()

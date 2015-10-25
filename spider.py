#!/usr/bin/env python3
# encoding: utf-8

import urllib.request
import requests
import re


def download(searchname):

        header = {'Host': 'sub.makedie.me',
                  'Pragma': 'no-cache',
                  'Referer': 'http://sub.makedie.me/',
                  'Upgrade-Insecure-Requests': '1',
                  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'}
        payload = {'searchword': searchname}
        url = 'http://sub.makedie.me/sub/'
        s = requests.Session()
        response = s.get(url, params=payload, headers=header)
        if response.status_code == requests.codes.ok:
            file = response.text
            return file
        else:
            print (response.status_code)
            return False


def cbk(a, b, c):

    #  @a:已经下载数据块的大小
    #  @b:数据块的大小
    #  @c:远程文件的大小
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print ('%.2f%%'% per)


def fliter(filename):

    f = open(filename, 'r')
    file_text = f.read()
    f.close()
    download_address = re.compile("(/download/\d+[^\"]+(?=\';return false))")
    subtitle_name = re.compile("([^/]+(?=';return false;))")
    all_file = re.findall(download_address, file_text)
    all_name = re.findall(subtitle_name, file_text)
    for index in range(len(all_file)):
        print ("正在下载第" + repr(index + 1) + "组字幕")
        urllib.request.urlretrieve('http://sub.makedie.me' + all_file[index], '/home/freecoding/sub/%s'% all_name[index], cbk)
    print ("下载完毕")


def main():

    name = input("电影/电视剧/纪录片名字?\n")
    season_No = input("第几季?电影等直接回车即可\n")
    set_No = input("第几集?电影等直接回车\n")
    final_name = name + season_No + set_No
    response_file = download(final_name)
    respose_txt = open('response.txt', 'w')
    respose_txt.write(response_file)
    respose_txt.close
    fliter('response.txt')


if __name__ == '__main__':
    main()

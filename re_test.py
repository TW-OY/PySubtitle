#!/usr/bin/env python
# encoding: utf-8

import re
import urllib


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
    download_address = re.compile("(/download/\d+[^\"]+(?=\';return false))")
    subtitle_name = re.compile("([^/]+(?=';return false;))")
    all_file = re.findall(download_address, file_text)
    all_name = re.findall(subtitle_name, file_text)
    for index in range(len(all_file)):
        print ("正在下载第" + repr(index + 1) + "组字幕")
        urllib.urlretrieve('http://sub.makedie.me' + all_file[index], '/home/freecoding/sub/%s'% all_name[index], cbk)
    print ("下载完毕")


fliter('filetemp.txt')

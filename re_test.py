#!/usr/bin/env python
# encoding: utf-8

import re
import urllib

def fliter(filename):

    f = open(filename,'r')
    file_text = f.read()
    pattern = re.compile("(/download/\d+[^"]+(?=\';return false))"])")
    all_file = re.findall(pattern,file_text)
    for item in all_file:
        print "正在下载第" +  repr(all_file.index(item)+1) + "组字幕"
        urllib.urlretrieve('http://sub.makedie.me'+item)
    print "下载完毕"
fliter('filetemp.txt')

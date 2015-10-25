#!/usr/bin/env python
# encoding: utf-8

import sys
import urllib2
import requests
import re
reload(sys)
sys.setdefaultencoding("utf-8")

def download(searchname):
        header = {
                  'Host':'sub.makedie.me',
                  'Pragma':'no-cache',
                  'Referer':'http://sub.makedie.me/',
                  'Upgrade-Insecure-Requests':'1',
                  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'}
        payload = {'searchword' : searchname}
        url = 'http://sub.makedie.me/sub/'
        s = requests.Session()
        response = s.get(url,params=payload,headers=header)
        if response.status_code == requests.codes.ok:
            file = response.text
        return file

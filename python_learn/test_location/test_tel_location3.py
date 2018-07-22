#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2018年3月26日

@author: 'lxq'
'''
import urllib
import urllib2
import HTMLParser


def get():
    postdata = urllib.urlencode(
        [('mobile', '18137899787'), ('action', 'mobile')])
    req = urllib2.Request('http://www.ip138.com:8080/search.asp')
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    fd = urllib2.urlopen(req, postdata, headers)
    h = fd.read()
    datas = HTMLParser.HTMLParser.feed(h)
    for data in datas:
        print data


get()

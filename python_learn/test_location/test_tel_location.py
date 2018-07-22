#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
from urllib import urlencode

#----------------------------------
# 手机号码归属地调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/11
#----------------------------------


def main():

    # 配置您申请的APPKey
    appkey = "0ea8e44e4612fb794c29f4979de48ef7"

    # 1.手机归属地查询
    request1(appkey, "GET")


def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/mobile/get"
    params = {
        "phone": "18137809737",  # 需要查询的手机号码或手机号码前7位
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json"  # 返回数据的格式,xml或json，默认json
    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]['province'], res["result"]['city']
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


def get_num_location(phone):
    # 配置您申请的APPKey
    appkey = "0ea8e44e4612fb794c29f4979de48ef7"
    url = "http://apis.juhe.cn/mobile/get"
    params = {
        "phone": phone,  # 需要查询的手机号码或手机号码前7位
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json"  # 返回数据的格式,xml或json，默认json
    }
    params = urlencode(params)
    f = urllib.urlopen(url, params)
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            return res["result"]['province'] + ' ' + res["result"]['city']
        else:
            return ''
    else:
        print "request api error"


if __name__ == '__main__':
    for i in xrange(2000):
        print i, get_num_location('13847963582')

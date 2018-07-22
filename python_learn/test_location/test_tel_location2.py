#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2018年3月26日

@author: 'lxq'
'''
import requests

PHONE_ATTR_JUHE = """http://apis.juhe.cn/mobile/get?phone={phone}"""
PHONE_ATTR_360 = """http://cx.shouji.360.cn/phonearea.php?number={phone}"""


def get_number_attribution_360(phone):
    """360查询号码归属地"""

    r = requests.get(PHONE_ATTR_360.format(phone=phone))
    result = r.json()

    province = result.get("data").get("province")

    if isinstance(province, unicode):
        province = province.encode("utf-8")
    else:
        province = province

    if not province:
        province = "null"
        city = "null"
    else:
        if province in ("北京", "天津", "上海", "重庆"):
            city = province
        else:
            city = result.get("data").get("city")

        if isinstance(city, unicode):
            city = city.encode("utf-8")
        else:
            city = city

    return (province, city)


def get_number_attribution(phone):
    """号码归属地查询
    1。聚合API
    2.360API"""
    try:
        phone = int(phone)
    except ValueError:
        return {"phone": phone, "province": "", "city": ""}

    r = requests.get(PHONE_ATTR_JUHE.format(phone=phone))
    result = r.json()

    if result.get("resultcode") == "200":
        province = result.get("result").get("province")
        city = result.get("result").get("city")

        if isinstance(province, unicode):
            province = province.encode("utf-8")
        else:
            province = province

        if isinstance(city, unicode):
            city = city.encode("utf-8")
        else:
            city = city

        res = {"phone": phone, "province": province, "city": city}
    else:
        res = get_number_attribution_360(phone)

    return res


if __name__ == "__main__":
    with open('phoneNum.txt', 'r') as f:
        for num in f:
            num = num.strip()
            atts = get_number_attribution(num)
            print num, atts[0], atts[1]

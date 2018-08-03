#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018年7月24日
@author: 'lxq'
@note: time模块功能
'''
import chardet
import time;  # 引入time模块

#时间戳
print "当前时间戳为:", time.time()
#时间戳->时间元祖
print "本地时间为 :", time.localtime(time.time())
print "本地时间为 :（localtime默认）",time.localtime()
#时间元祖->时间格式化 
print time.asctime( time.localtime() )#接受时间元组并返回一个可读的形式的字符串。格式化成Fri Aug 03 10:45:27 2018
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) #格式化时间，接收时间元祖，返回格式化字符串，本例时间格式同上 
# 格式字符串->时间戳
a = "Sat Mar 28 13:24:24 2016"
#格式化字符串->时间元组
print time.strptime(a,"%a %b %d %H:%M:%S %Y")
#时间元组->时间戳
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
#time 模块重要的属性
#time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）
print '本地市区与格林威治的偏移秒数:',time.timezone
#time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。
print chardet.detect(time.tzname[0])
print chardet.detect('我爱你')
print time.tzname[0].decode('GB2312')
print time.tzname[1].decode('GB2312')
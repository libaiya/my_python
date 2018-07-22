#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2018年3月26日
@note: 偏函数
@author: 'lxq'
'''
import functools
int2 = functools.partial(int, base=2)
print int2('10000')
# kw = { 'base': 2 }
# int('10010', **kw)
max2 = functools.partial(max, 10)
print max2(2, 4, 5)

#!/usr/bin/env Python
# -*- coding: utf-8 -*-
'''
Created on 2018年3月21日

@author: lxq
@note: 测试高阶函数
'''
print '***********hight_function***********'
f = abs
print f
#<built-in function abs>


def add(x, y, f):
    return f(x) + f(y)


print add(1, -3, abs)
# 4
# map,reduce
print '***********map***********'


def useMap(l):
    def toNomalStr(s):
        return s[0].upper() + s[1:].lower()
    return map(toNomalStr, l)


print useMap(['adam', 'LISA', 'barT'])
#['Adam', 'Lisa', 'Bart']

print '***********reduce***********'


def useReduce(l):
    return reduce(lambda x, y: x * y, l)


print useReduce([1, 2, 3, 4, 5])
# 120
print '***********filter***********'


def isPrimeNum(n):
    my_counter = 0
    for i in range(1, n):
        if n % i == 0:
            my_counter += 1
    if my_counter > 1:
        return False
    return True


print filter(isPrimeNum, [1, 2, 3, 4, 5, 6, 7, 8])
#[1, 2, 3, 5, 7]

print '***********sorted***********'

print sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=lambda x: x[1], reverse=True)

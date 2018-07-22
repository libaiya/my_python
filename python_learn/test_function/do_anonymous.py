#!/usr/local/bin/python2.7
# encoding: utf-8


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print L
L2 = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print L2
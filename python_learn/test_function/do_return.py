#!/usr/local/bin/python2.7
# encoding: utf-8


def createCounter():
    cnt = [0]

    def counter():
        cnt[0] += 1
        return cnt[0]
    return counter


counterA = createCounter()
print counterA(), counterA(), counterA(), counterA(), counterA()


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()


def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print f1(), f2(), f3()

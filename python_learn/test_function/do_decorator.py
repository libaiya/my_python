#!/usr/local/bin/env python
# encoding: utf-8
import time
import functools

print '************装饰器打印程序运行时间**************'


def metric(fn):
    def wrapper(*args, **kw):
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, end_time - start_time))
        return result
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0051)
    return x + y


f = fast(11, 22)

print '************装饰器打印日志**************'


def log(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print'begin call'
        fn(*args, **kw)
        print 'end call'
    return wrapper


@log
def hello():
    print 'hello world !'


hello()

print '************装饰器打印自定义日志**************'


def log2(text='start!'):
    def derector(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print text
            fn(*args, **kw)
        return wrapper
    return derector


@log2('aaa')
def hello2():
    print 'hello world2 !'


hello2()

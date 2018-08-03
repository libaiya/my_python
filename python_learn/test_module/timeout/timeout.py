#-*-coding:utf8-*-
'''
@author: lxq
@note: 监控函数时间超时函数
createdate：20180801
'''
import time
import signal

def timeout(interval):
    def wraps(func):
        def handler():
            raise RuntimeError()
        def deco(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(interval)
            res = func(*args, **kwargs)
            signal.alarm(0)
            return res
        return deco
    return wraps

if __name__=="__main__":
    @timeout(3)
    def test(i=5):
        time.sleep(i)
        print "%d sleep time"%(i)
        return i
    for i in xrange(1,10):
        try:
            i1=test(i)
            print i1
        except Exception,e:
            print '**********1'
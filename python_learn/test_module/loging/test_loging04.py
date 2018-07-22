#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2018年7月2日
@note: logging之日志回滚
@author: 'lxq'
logging的几种handle方式如下：
logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件
logging.FileHandler: 日志输出到文件

日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler
logging.handlers.BaseRotatingHandler
logging.handlers.RotatingFileHandler
logging.handlers.TimedRotatingFileHandler

logging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets
logging.handlers.DatagramHandler:  远程输出日志到UDP sockets
logging.handlers.SMTPHandler:  远程输出日志到邮件地址
logging.handlers.SysLogHandler: 日志输出到syslog
logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志
logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer
logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器
'''

import logging


from logging.handlers import RotatingFileHandler
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

##########################################################################
# 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler(
    'myapp.log', maxBytes=10 * 1024 * 1024, backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
# logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的
logging.getLogger('').addHandler(Rthandler)

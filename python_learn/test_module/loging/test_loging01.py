#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2018年7月2日
@note: 简单的将日志打印到屏幕
                默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
                日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
@author: 'lxq'
'''
import logging

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
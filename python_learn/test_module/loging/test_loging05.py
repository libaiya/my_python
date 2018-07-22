#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2018年7月2日
@note: logging之日志回滚
@author: 'lxq'
利用loging.cof配置文件实现功能
'''
# test_longing03.py
import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')


'''
#-----------------------------------------------------
# test_longing04.py
logger = logging.getLogger("example02")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018年7月24日
@author: 'lxq'
@note: time模块功能
'''
import chardet
import time;  # 引入time模块
from datetime import date,datetime,timedelta
now = date( 2018 ,  8 ,  03 )  
tomorrow = now.replace(day = 04 )  
#date
print 'date.max:', date.max  
print 'date.min:', date.min  
print 'date.today():', date.today()  
print 'date.fromtimestamp():', date.fromtimestamp(time.time())
print 'now:' , now,  ', tomorrow:' , tomorrow  
print 'timetuple():' , now.timetuple()  
print 'weekday():' , now.weekday()  
print 'isoweekday():' , now.isoweekday()  
print 'isocalendar():' , now.isocalendar()  
print 'isoformat():' , now.isoformat() 
#timedelta
delta = tomorrow - now  
print 'now:', now, ' tomorrow:', tomorrow  
print 'timedelta:', delta  
print now + delta  
print tomorrow > now
#time
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:00:30 2017

@author: 91432
"""

import urllib
import socket

#get类型请求
response=urllib.request.urlopen('http://www.baidu.com')  #百度首页源代码
print(response.read().decode('utf8'))

#post类型请求，需要传入data参数，data参数需要是dybt类型
#用urlencode把字典传过来，指定编码
#Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode（）编码
data=bytes(urllib.parse.urlencode({'adele':'hello from the other side'}),encoding='utf8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())

#超时的设置
try:
    response=urllib.request.urlopen('http://httpbin.org',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout): #用isinstance判断错误类型
        print('timeout')

#响应
response=urllib.request.urlopen('http://www.baidu.com')
print(type(response))
print(response.status)      #响应码
print(response.getheaders())  #头文件
print(response.getheader('Server'))
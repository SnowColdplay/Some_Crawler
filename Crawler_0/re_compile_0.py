# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:01:52 2017

@author: 91432
"""
#re.compile 把字符串编译为字符串对象，变成pattern模式
import re
content='hello from the other side'
pattern=re.compile('from.*?side')
result=re.findall(pattern,content)
print(result)

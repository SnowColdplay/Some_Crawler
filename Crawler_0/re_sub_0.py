# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:01:39 2017

@author: 91432
"""
#re.sub用来做字符串的替换
import re
#==============================================================================
# content='1989 is a great album'
# content=re.sub('\d+','Red',content)
# print(content)
#==============================================================================

#如果要替换的目标包含原来的字符串，把要匹配的字符串加一个括号
#可以替换为空格
content='1989 are great albums'
content=re.sub('(\d+)',r'\1 and Red',content)
print(content)

#strip方法可以去掉换行符
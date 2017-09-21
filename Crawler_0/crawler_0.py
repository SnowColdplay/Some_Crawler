# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:10:55 2017

@author: 91432 整理自天善智能爬虫
"""
import requests

#请求和响应的过程
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
response=requests.get('http://www.google.com',headers=headers)
print('response的内容是',response.text)
print('response的头文件是',response.headers)
print('response的状态码是',response.status_code)

#图片表示形式为二进制流，把二进制流保存成图片
response=requests.get('https://www.google.com.hk/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
print('图片response的内容是',response.content)
#写入
with open('google.png','wb') as f:
    f.write(response.content)
    f.close()
    


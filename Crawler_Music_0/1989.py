# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:42:34 2017

@author: 91432
"""
import requests
import json
import re
#lrc_urlhttp://music.163.com/weapi/song/lyric?csrf_token=16150d2c10029e1ba7c3ddc14abb02e0
#要作token验证，比较麻烦
lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(21563184) + '&lv=1&kv=1&tv=-1'
#id是歌曲的id
each_lyric=requests.get(lrc_url)
#print(lyric.text)
json_obj = each_lyric.text
j = json.loads(json_obj)
#==============================================================================
english_lyric = j['lrc']['lyric']
chinese_lyric=j['tlyric']['lyric']
english_lyric = re.sub('\[.*?]', "", english_lyric).strip()
chinese_lyric = re.sub('\[.*?]', "", chinese_lyric).strip()
print(english_lyric)
print(chinese_lyric)
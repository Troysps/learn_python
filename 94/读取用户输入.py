# -*- coding:utf-8 -*-

# 下面使用json.load()读取文件
import json

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back,",username)
    

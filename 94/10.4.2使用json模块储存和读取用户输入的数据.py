# -*- coding:utf-8 -*-
# 10.4.2 使用json模块保存和读取用户生成的数据
import json

username = input("Your name: ")
filename = 'username.json'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We will remember you when you back",username)
    


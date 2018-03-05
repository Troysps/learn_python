# -*- coding:utf-8 -*-
# 10.4 存储数据

# 10.4.1 使用json模块以及json.dump()储存文件
import json

number = [2, 3, 5, 6, 7, 19]

filename = 'number.json'

with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

# 接下来使用json模块中的json.load()用于读取文件
import json

filename = 'number.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    
print(numbers)

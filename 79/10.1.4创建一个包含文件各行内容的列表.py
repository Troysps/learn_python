# -*- coding:utf-8 -*-
# 10.1.4 创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
    


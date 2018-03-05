# -*- coding:utf-8 -*-
# 10.1.6 处理大型文件 一百万位的大型文件

filename = 'π的一百万位-1.txt'

with open(filename) as file:
    lines = file.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string[:52],"......")
print(len(pi_string))

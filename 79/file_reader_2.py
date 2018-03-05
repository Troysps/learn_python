# -*- coding:utf-8 -*-
# 10.1.2 文件路径
# 在windows系统下查找txt文件 并用Python解释器将其读取

a = r'D:\PY程序\79\pi_digits.txt'

with open(a) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    
    

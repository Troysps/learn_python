# -*- coding:utf_8 -*-
# 第十章 文件和异常

# 10.1.1 读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 使用了关键字with 函数open() as关键字 read()函数
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    

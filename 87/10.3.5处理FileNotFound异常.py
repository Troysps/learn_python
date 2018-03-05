# -*- coding:utf-8 -*-
# 10.3.5 处理FileNotFoundError异常
filename = 'alice.txt'

with open(filename) as file_object:
    contents = file_object.readlines()
    

# 同样使用try-except-else代码库进行尝试
filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.readlines()
except FileNotFoundError:
    print("Sorry,the file",filename,"does not exict")
    

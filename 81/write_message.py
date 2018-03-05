# -*- coding:utf-8 -*-

# 10.2 写入文件
# 读取模式'r' 写入模式'w' 附加模式'a'
# 10.2.1 写入空文件
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love Python')
    
    
     
# 10.2.2 写入多行 注意这里没有换行 需要自己添加换行符
with open(filename, 'w') as file_object:
    file_object.write("I love Python.\n")
    file_object.write("I love Programming.\n")
    file_object.write("I love myself.\n")
    file_object.write("I love 黄郴红.\n")


# 10.2.3 附加到文件 使用附加模式 'a'
with open(filename, 'a') as file_object:
    file_object.write("I love my family.")

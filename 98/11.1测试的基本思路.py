# -*- coding:utf-8 -*-
# 这是阐述测试的基本思路 
# 使用导入模块函数 与while循环输入 不断的测试输入各种值

from name_function import get_formatted_name
print("Enter 'q' to quit at any time.")
while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break
    last = input("Enter your last name: ")
    if last == 'q':
        break
        
    formatted_name = get_formatted_name(first, last)
    print(formatted_name)


# 上述的代码通过 import 导入函数
# while循环不断输入数据进行 测试函数
# 这就是测试函数的基本思路

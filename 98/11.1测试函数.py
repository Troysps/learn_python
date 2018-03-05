# -*- coding:utf-8 -*-
# 11.测试代码

# 11.1 测试函数
# 首先了解测试函数的基本思路
# 先编写一个函数
def get_formatted_name(first, last):
    """generate a neatly formatted full name"""
    full_name = first + " " +last
    return full_name.title()
    
print(get_formatted_name('lei', 'tianfu'))

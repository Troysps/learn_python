# -*- coding:utf-8 -*-
# 11.测试代码

# 11.1 测试函数
# 首先了解测试函数的基本思路
# 先编写一个函数
def get_formatted_name(first, last):
    """generate a neatly formatted full name"""
    full_name = first + " " +last
    return full_name.title()
    
def get_middle_name(first, middle, last):
    """生成整洁的名字"""
    full_name = first + " " + middle + " " + last
    return full_name

def get_right_name(first, last, middle=''):
    """生成整洁的名字"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
        
    return full_name.title()

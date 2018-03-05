# -*- coding:utf-8 -*-
# 11.1.4 测试没有通过时 意味着你编写的函数代码有问题不能到达预定的效果
# 对函数进行修改

def get_formatted_name(first, last, middle=''):
    """生成整洁的名字"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
        
    return full_name.title()
    
# 函数修改完成再编写测试用例进行测试

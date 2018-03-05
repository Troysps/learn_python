# coding=gbk
# 函数练习6 将函数存储在模块中 
# 使用import 语句

def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMake a",str(size),"inch pizza with the following toppings:")
    for topping in toppings:
        print("-",topping)

# -*- coding:utf-8 -*-
# 练习11-3 编写一个类
class Employee():
    """编写一个雇员的类"""
    
    def __init__(self, first_name, last_name, salary):
        """特殊方法 设定属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
        self.raise_salary = []
    
    def give_raise(self, raise_salary=5000):
        """默认薪水上涨5000 但是也接受其他的上涨数额"""
        self.salary += raise_salary

employ_1 = Employee('lei', 'tianfu', 2000)

employ_1.give_raise()
employ_1.give_raise(10000)

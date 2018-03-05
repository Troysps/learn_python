# -*- coding:utf-8 -*-
# 编写测试
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""
    
    def setUp(self):
        """创建一个调查对象以及一组答案"""
        first_name = 'lei'
        last_name = 'tianfu'
        salary = 2000
        self.employ_1 = Employee(first_name, last_name, salary)
        self.raise_salary = [5000, 10000, 20000]
        
    def test_give_default_salary(self):
        """测试默认薪资涨幅"""
        self.employ_1.give_raise(self.raise_salary[0])
        self.assertEqual(7000,self.employ_1.salary)

unittest.main()

# -*- coding:utf-8 -*-
# 11.1 单元测试和用例测试
# 单元测试：用于核实函数的某个方面是否存在问题
# 测试用例：是一组单元测试
# 全覆盖测试：包含一整套的单元测试,涵盖了函数可能使用到的地方

# 11.1.2 可通过的测试 要为函数编写测试用例 首先可导入模块unittest 以及函数
# 再创建继承unittest.TestCase的类 并编写一系列方法对函数行为的不同方面进行测试


# 第一步导入unittest 以及要测试的函数
import unittest
from name_function import get_formatted_name,get_middle_name,get_right_name


# 第二步 创建一个继承unittest.Case的类 并编写方法进行测试
class NameTest(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        # 这里方法必须test_打头 将自动运行该测试
        """能够正确的处理Lei Tianfu这样的名字么"""
        formatted_name = get_formatted_name('lei', 'tianfu')
        self.assertEqual(formatted_name, 'Lei Tianfu')
        #assertEqual()断言方法 这是测试函数的核心方法

    def test_first_middle_last_name(self):
        """是否可以正确的处理Lei Tianfu这样的名字"""
        middle_name = get_middle_name('lei', 'tianfu')
        self.assertEqual(middle_name, 'Lei Tianfu')
                
    def test_first_last_middle_name(self):
        """是否能够正确的使用 Jen Shi Bang这样的名字么"""
        right_name = get_right_name(
            'jen', 'bang', 'shi')
        self.assertEqual(right_name, 'Jen Shi Bang')

unittest.main()        

# unittest.main()让Python运行这个文件中的测试
# 把三个测试结合起来 结果又句点有E 而且明确指出了是第二个测试的错误

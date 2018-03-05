# -*- coding:utf-8 -*-

# 11.1.3 测试没有通过
import unittest
from name_function import get_middle_name

class MiddleNameTest(unittest.TestCase):
    """测试name_function中的get_middle_name函数"""
    
    def test_first_middle_last_name(self):
        """是否可以正确的处理Lei Tianfu这样的名字"""
        middle_name = get_middle_name('lei', 'tianfu')
        self.assertEqual(middle_name, 'Lei Tianfu')
        
unittest.main()


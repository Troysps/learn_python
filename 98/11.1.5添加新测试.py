# -*- coding:utf-8 -*-
# 11.1.5 添加新测试

import unittest
from name_function_1 import get_formatted_name

class NameAddTest(unittest.TestCase):
    """测试name_funtion_1 中的函数get_formatted_name"""
    
    def test_first_last_middle_name(self):
        """是否能够正确的使用 Jen Shi Bang这样的名字么"""
        formatted_name = get_formatted_name(
            'jen', 'bang', 'shi')
        self.assertEqual(formatted_name, 'Jen Shi Bang')
        
unittest.main()


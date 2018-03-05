# -*- coding:utf-8 -*-
# 测试city_functions.py中的函数

import unittest
from city_functions import describe_city,describe_city_2

class CityWhereTest(unittest.TestCase):
    """测试city_function.py中的函数describe_city"""
    
    def test_city_country(self):
        """是否可以正确处理Santiago, chile"""
        city_describe = describe_city('santiago', 'chile')
        self.assertEqual(city_describe, 'Santiago, Chile')

    def test_city_country_2(self):
        """是否可以正确处理Santiago, chile"""
        city_describe = describe_city_2('santiago', 'chile')
        self.assertEqual(city_describe, 'Santiago, Chile')

    def test_city_country_population(self):
        """
        测试函数desribe_city_2 是否可以正确处理Santiago, Chile -Population 50000
        """
        city_describe = describe_city_2('santiago', 'chile', 50000)
        self.assertEqual(city_describe, 'Santiago, Chile -Population 50000')





unittest.main()

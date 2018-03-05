# -*- coding:utf-8 -*-
# 11.1 测试函数练习
# part 1 编写要测试的函数

def describe_city(city, country):
    """返回格式为city, country的字符串"""
    city_where = city + ", " + country
    return city_where.title()

def describe_city_2(city, country, population=''):
    """返回格式为city, country的字符串"""
    if population:
        city_where = city + ", " + country + ' -population ' + str(population)
    else:
        city_where = city + ", " + country
    return city_where.title()

# 测试函数必须是字符串的形式str 转化成数字可以用int方法提出出来使用

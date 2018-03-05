# -*- coding:utf-8 -*-
# 10.1.3 逐行读取 使用for循环遍历文件中的每一行

n = 'pi_digits.txt'
with open(n) as lines:
    for line in lines:
        print(line.strip())


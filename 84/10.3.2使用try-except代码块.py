# -*- coding:utf-8 -*-
# 10.3.2 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")

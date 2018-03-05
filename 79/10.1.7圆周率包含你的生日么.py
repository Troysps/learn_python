# -*- coding:utf-8 -*-
# 10.1.7 圆周值中包含你的生日么

filename = 'π的一百万位-1.txt'

with open(filename) as file:
    lines = file.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Please enter your birthday. ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi.")
else:
    print("Yuo birthday not in the first million digits of pi.")

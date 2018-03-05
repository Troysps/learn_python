# -*- coding:utf-8 -*-
# 10.3.4 避免程序崩溃
# 使用try-except-else
print("Give me two numbers, and I will division them.")
print("Enter 'q' to quit at any time.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't division by 0!")
    else:
        print(answer)

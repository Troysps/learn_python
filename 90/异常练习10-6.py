# -*- coding:utf-8 -*-
# 10.6-10.7 处理异常 使用try-except-else代码块
print("Give me two numbers,and I will division them.")
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
    except ValueError:
        print("Sorry ,You must provide numbers.")
    except ZeroDivisionError:
        print("Zero can't be division.")
    else:
        print(answer)



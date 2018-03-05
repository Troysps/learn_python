# -*- coding:utf-8 -*-
# 10.3.3 使用异常避免崩溃
print("Give me two number, and I will division them")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number)/int(second_number)
    print(answer)
    
# 这里就是错误的示范 使得用户看见了系统崩溃及其原因



# -*- coding:utf-8 -*-
# 10.2 写入文件练习

# part_1 将写入文件和用户输入相结合 以及while循环
usernames = ''
while True:
    username = input("Please enter your name: ")
    print("Enter 'q' to quit at any time.")
    
    if username != 'q':
        print("\nHello,",username,".")
        usernames += username+"\n"
        
    else:
        break



filename = 'guest.txt'
filename_1 = 'like_reasons.txt'

with open(filename, 'a') as file_object:
    file_object.write(usernames)

# part_2 while循环加上用户输入 导入到文件文本中 询问用户为啥喜欢编程
like_programming = ''
总数 = []

while True:
    reason = input("Why you like programming? ")
    print("Enter 'q' to quit at any time.")

    if reason != 'q':
        like_programming += reason+"\n"
        总数.append(reason)
    else:
        break

reasons = str(len(总数))

with open(filename_1, 'w') as n:
    n.write(like_programming)
    n.write(reasons)

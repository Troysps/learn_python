# coding=gbk
# while循环简介

# part_1 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
# part_2 让用户选择何时退出
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = " "
while message != 'quit':
    message = input(prompt)
    print(message)
    
# 小技巧使用if语句消除输出quit
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = " "
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
print("\n")
# part_3 使用标志
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)

# part_4 使用break退出循环
prompt = "\nPlease enter the name of city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go "+ city.title() + "!")
        

# part_5 在循环中使用continue语句
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

# part_6 避免无限循环

# coding=gbk
# 外星人颜色_1 简单if语句(两个版本 一个通过了 一个没通过）
alien_color = ['green','yellow','red']
color = 'green'
if color == 'green':
    print("Player get 5 points!")
if color != 'green':
    print("Player get 10 points!")
print("\n")
# 外星人颜色_2 if_else结构(两个版本 一个定义颜色 一个没有)
alien_color = ['green','yellow','red']
color = 'green'
if color == 'green':
    print("Player get 5 points!")
else:
    print("Player get 10 points!")
print("\n")
for color in alien_color:
    if color == 'green':
        print("Player get 5 points!")
    else:
        print("Player get 10 points!")
print("\n")
# 外星人颜色_3 if_elif_else结构
alien_color = ['green','yellow','red']
color = 'red'
if color == 'green':
    print("Player get 5 points.")
elif color == 'yellow':
    print("Player get 10 points.")
else:
    print("Player get 15 points.")
print("\n")
# 版本2
color = 'yellow'
if color == 'green':
    print("Player get 5 points.")
elif color == 'yellow':
    print("Player get 10 points.")
else:
    print("Player get 15 points.")
alien_color = ['green','yellow','red']
print("\n")
# 版本3
color = 'green'
if color == 'green':
    print("Player get 5 points.")
elif color == 'yellow':
    print("Player get 10 points.")
else:
    print("Player get 15 points.")
alien_color = ['green','yellow','red']
print("\n")
# 解释
for color in alien_color:
    if color == 'green':
        print("Player get 5 points.")
    elif color == 'yellow':
        print("Player get 10 points.")
    else:
        print("Player get 15 points.")
# 人生的不同阶段
print("\n")
age = 21
if age < 2:
    print("You are a baby.")
elif (age >= 2) and (age < 4):
    print("You are learning walk!")
elif (age >= 4) and (age < 13):
    print("You are a child.")
elif (age >= 13) and (age < 20):
    print("You are a teenager.")
elif (age >= 20) and (age < 65 ):
    print("You are an adult.")
elif age >= 65:
    print("You are an old man.")
print("\n")
# 喜欢的水果
favorite_fruit = ['banana','apple','cucumber','peach','durian']
if 'banana' in favorite_fruit:
    print("U really like bananas.")
if 'apple' in favorite_fruit:
    print("U really like apples.")
if 'pizza' in favorite_fruit:
    print("U really like cucumber")
if 'peach' in favorite_fruit:
    print("U really like peaches.")
if 'dragon fruit' in favorite_fruit:
    print("U really like durian.")

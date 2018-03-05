# coding=gbk
# 简单if语句
age = 19

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
print("\n")    
# if_else语句
age = 17

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
print("\n")
# if_elif_else结构
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
print("\n")    
# 代码更加简洁
age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your adimission cost is $"+str(price)+".")
print("\n")
# 使用多个elif代码块
age = 88

if age <= 4:
    price = 0
elif age <= 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your adimission cost is $"+str(price)+".")
print("\n")
# 省略else代码块 if_elif结构可用
age = 15

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
    
print("Your adimission cost is $"+str(price)+".")
print("\n")
# 测试多个条件
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
print("\n")
# 测试多个条件 if_elif结构行不通
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

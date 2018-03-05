# coding=gbk
# 编写函数

# part_1 定义函数 关键字def
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
    
greet_user()
print("\n")

# part_1.1 向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
    
greet_user('ten')
print("\n")

# part_1.2 实参和形参
def lover(name,age):
    """显示爱人的名字以及年龄"""
    print(name + ", 今年 "+ str(age) +"岁.")
    
lover('黄郴红',21)

# 如上所示 name age 是形参  '黄郴红',21是实参

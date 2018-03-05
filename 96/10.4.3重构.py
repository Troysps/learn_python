# -*- coding:utf-8 -*-
# 10.4.3 重构
# 重构就是将代码划分为一系列完成具体工作的函数

# 代码重构 part1
import json

def greet_user():
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("Your name: ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We will remember you when you back,",username)
    else:
        print("We will remember you when you back,",username)
greet_user()

# 重构2

def get_stored_username():
    """如果储存了用户名 就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
        
def greet_user():
    """问候用户并指出名字"""
    username = get_stored_username()
    if username:
        print("hei",username)
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print(username)

greet_user()


# 重构3
def get_stored_username():
    """如果存储了用户数据 就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
        
def get_new_username():
    """提示用户输入新的用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
    
def greet_user():
    """问候用户 并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back,",username,"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back,",username,"!")
        
greet_user()

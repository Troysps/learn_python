# -*- coding:utf-8 -*-
# 10.4 重构练习

# part 1 提示用户输入一个数字 存储并读取用户输入
import json
def user_number():
    """
    提示用户输入数字
    存储并读取用户输入
    """
    filename = 'user_number.json'
    
    try:
        with open(filename) as f_obj:
            user_number = json.load(f_obj)            
    except FileNotFoundError:
        user_number = input("Enter your favorite numebr: ")
        with open(filename , 'w') as f_obj:
            json.dump(user_number, f_obj)
            print("Your favorite number is:",user_number)
    else:
        print("Your favorite number is:",user_number)
        
user_number()

# 全局变量和局部变量 知识点

# part 2 假设前后用户不是同一人
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

def exam_username():
    """检查用户名是否错误"""
    username = input("Your name: ")
    exam = input("Are you sure right ,yes or no ")
    if exam == 'yes':
        return username
    else:
        return get_new_username()
    

def greet_user():
    """问候用户 并指出其名字"""
    username = exam_username()
    if username in get_stored_username():
        print("Welcome back,",username,"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back,",username,"!")
        
greet_user()

# 不完美程序 没有每次进行检查 以及不能遍历json文件内容
# 分为几种情况 第一种 我输入对了 确认也是对的
# 第二种 我输入错的 我也知道错的 重新输入

# 第三种 我以为 输入对了 但是错了 重新输入
# 第四种 我以为输入错了 但是是对的 这里也会重新输入

# 这里的第三种和第四种情况没有解决

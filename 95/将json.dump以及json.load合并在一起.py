# -*- coding:utf-8 -*-
# 使用json.dump() 以及json.load() 合并在一起
import json

# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
def greet_user():
    filename = "'uesrname.json'"

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

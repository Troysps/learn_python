# coding=gbk
# 用户输入和while循环自发练习
# 1.猜数字小游戏
# 2.用户输入和移动列表元素相结合-模拟用户注册


# 1.猜数字小游戏
print("现在我们来做一个猜数字小游戏吧，数值在0到100之间.")
number = 66

while True:
    guess_number = input("输入你猜的数值吧! ")
    message = int(guess_number)
    
    if message > 66:
        print("提示:数值没那么大")
        
    elif (message < 66) and (message > 60):
        print("提示:还差一点.")
        
    elif (message <= 60) and (message >= 0):
        print("提示:数值没这么小")
        
    elif message == 66:
        print("提示:恭喜你猜对了")
        break
print("\n")
# 2.模拟用户注册
new_user = []
confirmed_users = ['唐倩','雷天夫','蔡家栋','张蕾','张兴宇']

while True:
    prompt = "请输入你的用户名: "
    username = input(prompt)
    new_user.append(username)    
    
    if username in confirmed_users:
        print("您的用户名已被注册")

    elif username not in confirmed_users:
        confirmed_users.append(username)
        print("您已注册成功并且通过验证")
        
    message = input("是否继续注册: ")
    if message == '否':
        break
# 显示已通过验证的所有用户以及最近输入的全部用户
print(new_user)

print(confirmed_users)


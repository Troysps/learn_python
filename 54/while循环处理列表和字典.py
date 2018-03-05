# coding=utf-8
# 用while循环处理列表和字典

# part_1 在列表之间移动元素
# 首先创建一个未验证用户的列表
# 再创建一个存储已经验证用户的空列表
uncomfirmed_users = ['jen','ten','lei']
comfirmed_users = []
# 验证每个用户直到没有为止
# 将每个验证的用户存储到已验证用户中
while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()
    
    print("Verifying user : " + current_user.title())
    comfirmed_users.append(current_user)
    
# 显示所有已经验证的用户
print("\nThe following users have been comfirmed : ")
for comfirmed_user in comfirmed_users:
    print(comfirmed_user.title())
print("\n")
# 利用方法pop()在未验证列表中提取并且删除元素
# 拓展：尝试假设已验证的用户中有存在元素 提示用户在输入之后 您的用户名已被注册
# 但是不影响其他的用户输入 变成已验证的用户输入

# part_2 删除包含特定值的所有列表元素
pets = ['cat','cat','cat','dog','goldfish','rabbit']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
print("\n")
# 和函数set()完全不同 这是方法remove()

# part_3 使用用户输入来填充字典
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将回答与人名做成字典
    responses[name] = response
    # 设置循环停止的路径
    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name+" would you like to climb " + response + ".")
            

# 可以尝试先让用户选择是否参与回答

# 做一个数字游戏

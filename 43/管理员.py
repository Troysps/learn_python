# coding=gbk
# 处理列表特殊元素
usernames = ['admin','troy','alibaba','apple','huawei']
for name in usernames:
    if name == 'admin':
        print("Hello "+name.title()+",would you like to see a status report?")
    else:
        print("Hello "+name.title()+",thank you for logging in again.")
print("\n")
# 处理空列表
usernames = []
if usernames:
    for name in usernames:
        print("Hello "+name.title()+"!")
else:
        print("We need finding some users!")

print("\n")
# 检查用户名
current_users = ['apple','huawei','facebook','ins','goole','mircosoft']
new_users = ['xiaomi','huawei','lenovo','Goole','mircosoft']
for user in new_users:
    if user in current_users:
        print("Enter another username.Please.")
    else:
        print("The username is not applicable.")
print("\n")
# 序数
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+"nd")
    elif number == 3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")

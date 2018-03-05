# coding=utf-8
# 用户输入和while循环练习

# part_1 列表之间转移元素
sandwich_orders = ['fruit sandwish','tuna sandwish','beef sandwish']
finished_sandwiches = []
# 循环sandwich_orders并且提取其中的元素
while sandwich_orders:
    order = sandwich_orders.pop()
    print("\tsandwiches : "+ order.title())
    
    finished_sandwiches.append(order)
# 显示所有已验证的sandwiches
print("\nThe following sandwich have been comfirmed:")
for finished in finished_sandwiches:
    print(finished)
print("\n")
# part_2 删除列表中的特定值
sandwich_orders = ['fruit sandwish','tuna sandwish','beef sandwish']
for order in range(3):
    # 这里只是单纯的告诉我们这个循环多少次，每执行一次就创建一个pastrami sandwich
    new_order = 'pastrami sandwich'
    sandwich_orders.append(new_order)
    
print(sandwich_orders)

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

print("\n"+str(sandwich_orders))

# part_3 使用用户输入和while循环充填字典
users_responses = {}

# 设置标志
active = True

while active:
    # 提示用户输入
    name = input("Hei!Plz enter your name: ")
    place = input("One place in the world , where would you go? ")
    # 将用户输入组成字典
    users_responses[name] = place

    repeat = input("Enter 'quit':quit the responses. ")
    if repeat == 'quit':
        active = False
# 显示调查结果
for name,place in users_responses.items():
    print(name+" : "+place)

# coding=gbk

# 函数处理列表_part4
# 函数可以处理任意大小的列表
def greet_user(names):
    """向列表中的每位用户发出问候"""
    for name in names:
        msg = "Hello," + name.title() + "!"
        print(msg)
usernames = ['ten','lei','tianfu']
greet_user(usernames)
print("\n")
# part_4.1 利用函数简化列表之间的传递流程

# while循环传递列表之间的元素
# 首先创建两个列表 一个空列表 一个非空列表
unprinted_designs = ['iphone cases','robot pendant','dodacahedron']
completed_models = []

# 模拟打印每个设计，知道没有为止
# 将打印好的设计，移动到列表completed_models
while unprinted_designs:
    current_design = unprinted_designs.pop()
    
    # 模拟根据设计制作3D打印模型的过程
    print("Printing model:",current_design)
    completed_models.append(current_design)
    
# 显示打印好的所以模型
print("\nThe following models have been printed:")
print(completed_models)

print("\n")
# 现在使用函数简化 并使得列表有无限的修改可能
# 创建两个函数 第一个函数体表示 模拟打印每个设计 并将其移动到已打印的列表
# 第二个函数体表示 显示打印好的所有模型

# 第一个函数
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移动到列表completed_models里
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # 模拟根据设计制作的3D打印模型过程
        print("Printing model:",current_design)
        completed_models.append(current_design)
        
# 第二个函数
def show_printed_models(completed_models):
    """显示已打印的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    
unprinted_designs = ['lei','tian','fu']
completed_models = []

print_models(unprinted_designs,completed_models)
show_printed_models(completed_models)


print("\n")
# part4.2 禁止函数修改列表 利用切片表示法创建列表的副本

# 在数据分析里面 原始数据尤为重要 所以要牢记切片表示法
unprinted_designs = ['huang','cheng','hong']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_printed_models(completed_models)

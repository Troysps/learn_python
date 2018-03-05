# coding=gbk
# 函数练习6 将函数存储在模块中 
# 应用函数
import show_printed_model


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


n = ['s','d','e']
m = []
print_models(n,m)
show_printed_model.show_printed_models(m)

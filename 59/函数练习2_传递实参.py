# coding=gbk
# 函数练习_2 传递实参

# part_2.1 位置实参 每个实参都有相对应的形参
def describe_pets(animal_type,pet_name):
    """显示宠物的种类和名字"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pets('dog','sam')
# 顺序错误示范 形参和实参的顺序一一对应
describe_pets('sam','dog')
# 发生了明显的语法错误

# 通过上述的演示可以发现 位置实参的两点明显的特点
# part_2.1.1 可以调用函数多次
# part_2.1.2 位置实参的顺序极其重要

# part_2.2 关键字实参 对实参进行赋值 这样顺序就无关紧要
describe_pets(pet_name='sam',animal_type='dog')
# 值对 在实参中将形参和值关联起来 不需要考虑顺序

# Part_2.3 默认值 给每个形参指定默认值
def describe_pets(pet_name,animal_type='dog'):
    """显示宠物的种类和名字"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pets(pet_name='jen')

# 这里特意修改了形参的位置 最简单的写法应当如下:
describe_pets('ten')

# part_2.4 等效的函数调用 传递函数的三种方法:位置实参 关键字实参 默认值 可以混用

# part_2.5 避免实参错误 发生语法错误的时候回看 Traceback 


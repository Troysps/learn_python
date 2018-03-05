# coding=gbk
# 函数练习

# part_1 编写函数并调用
def display_message(topic):
    """第八章学习函数"""
    print("Chapter 8 learning " + topic.title() + ".")

display_message('functions')
print("\n")

# part_2 编写函数包含形参 应用实参
def favorite_book(title):
    """最喜欢的书本"""
    print("One of my favorite book is "+title.title())

favorite_book('alice in wonderland')
favorite_book('learning python')

# 尝试只有一个形参的时候是否可以对应无限的实参
favorite_book('python','nnnnn')
# 形参和实参一一对应!



# coding=gbk
# 函数part_3 返回值 活用return语句

# part_3.1 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()
    
musician = get_formatted_name('jen', 'hex')
print(musician)

# return语句返回调用函数的代码行
# 调用返回值的函数需要加上变量

# part_3.2 让实参变成可选 根据位置实参 使用默认值可以让实参变成可选
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " +middle_name + " " + last_name
    return full_name.title()
    
musician = get_formatted_name('jen' , 'lei', 'fu')
print(musician)

# 假如姓名中间没有 那么可以调整形参的位置 以及默认值
def get_formatted_name(first_name, last_name, middle_name = ''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + " " +middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
    
musician = get_formatted_name('lei', 'fu')
print(musician)

musician = get_formatted_name('lei', 'fu' ,'tian')
print(musician)

# if语句 位置实参 默认值

# part_3.3 返回字典 函数体中可以设置 字典 列表 字符串 数值 用一个变量表示
def build_person(first_name, last_name):
    """返回一个字典， 其中包含有关一个人的信息"""
    person = {'first' : first_name, 'last' : last_name}
    return person
    
musician = build_person('jen', 'hex')
print(musician)

#  返回字典 存储年龄
def build_person(first_name, last_name, age = ''):
    """返回一个字典 其中包含有关一个人的信息"""
    person = {
    'first' : first_name,
    'last' : last_name,
    }
    if age:
        person['age'] = age
    return person
    
musician = build_person('jen', 'ten', age=27)
print(musician)

# part_3.4 结合使用函数和while循环 
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()
    
# 建立循环
while True:
    print("\nPlease tell me your name : ")
    print("Enter 'q' at any time quit.")
    f_name = input("First name : ")
    
    if f_name == 'q':
        break

    l_name = input("Last name : ")
    if l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    

    

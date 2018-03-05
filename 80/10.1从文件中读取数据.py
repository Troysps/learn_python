# -*- coding:utf-8 -*-
# 10.1 文件和异常 
# 10.1 练习

# part_1 Python 学习笔记
# 读取整个文件 使用方法read()
filename = 'Python学习.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


print("\n")
# 打印时遍历文件
with open(filename) as file_object_1:
    contents_1 = file_object_1.readlines()
    for line in contents_1:
        print(line.rstrip())

print("\n")
# 将各行储存在一个列表中
with open(filename) as file_object_2:
    contents_2 = file_object_2.readlines()
    
learn_py = ''
for line in contents_2:
    learn_py += line.strip()
    
print(learn_py)

print("\n")
# 注意此处 一定要在创建变量 变量为空字符串 接for循环 在+= 这里加方法strip()

# part_2 使用方法replace()替换目标文件中的某一字符串

with open(filename) as file_replace:
    lines = file_replace.read()
    c = lines.replace('Python', 'C')
    print(c)


# 这里只能使用方法read() 下面尝试方法readlines()

with open(filename) as file_1:
    lines = file_1.readlines()
    
py = ''
for line in lines:
    py += line.rstrip()
    
c = py.replace('Python', 'C')
print(c)

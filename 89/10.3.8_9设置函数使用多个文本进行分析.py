# -*- coding:utf-8 -*-
# 10.3.7 使用多个文件
# 通过设置函数使得文本分析 文本输入变得简易以及可重复

def count_words(filename):
    """计算一个文件大概包含多少个单词"""
    
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry,the file ",filename,"does not exist."
        print(msg)
    else:
    # 计算alice书中有多少个单词
        words = contents.split()
        num_words = len(words)
        print("The flie",filename,"has about",str(num_words),"words.")
    
filename = 'Alice in Wonderland.txt'
count_words(filename)

# 应该是在哪个部分代码打错了 filename有关的打错了

print("\n")
# 10.3.8 失败时一声不吭 使用pass语句
def count_words(filename):
    """计算一个文件大概包含多少个单词"""
    
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
    # 计算alice书中有多少个单词
        words = contents.split()
        num_words = len(words)
        print("The flie",filename,"has about",str(num_words),"words.")
    
filenames = ['Alice in Wonderland.txt', 'like_reasons.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)

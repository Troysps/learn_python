# -*- coding:utf-8 -*-
# 10.10 使用方法count()计算常用单词的频次

file_1 = 'Alice in Wonderland.txt'

def count_alice_words(filename):
    """计算在爱丽丝梦游仙境里 alice一次出现了多少次"""
    
    try:
        with open(filename) as n:
            contents = n.read()
    except FileNotFoundError:
        pass
    else:
        # 这里使用方法lower()以及count()
        print(contents.lower().count('alice'))

count_alice_words(file_1)

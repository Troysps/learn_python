# -*- coding:utf-8 -*-
# 10.3.6 分析文本

filename = 'Alice in Wonderland.txt'

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
    

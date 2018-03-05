# -*- coding:utf-8 -*-
# 10.8 喵和狗 读取文件并且打印打屏幕上
file_1 = 'cats.txt'
file_2 = 'dogs.txt'
file_3 = 'Alice in Wonderland.txt'

def file_read(filename):
    """用函数避免程序崩溃"""
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        """计算文件中包含多少个单词"""
        words = contents.split()
        # 方法split()是把一个个的单词分割提取变为列表
        # 所以还有加上函数len()进行计算列表中有多少的元素
        num_words = len(words)
        print(str(num_words))
        
file_read(file_1)
file_read(file_2)
file_read(file_3)



# 10.9 在上面的函数中加上pass语句

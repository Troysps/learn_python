# coding=gbk
# 函数学习6 将函数存储在模块中

# part_6.1 导入整个模块
# 格式：import语句 函数名
import pizza

pizza.make_pizza(18,'apple')
pizza.make_pizza(233,'apple','banana','beef')

# part_6.2 导入特定的函数 模块中特定的函数
# 格式：from 文件名 import 函数名

from pizza import make_pizza

pizza.make_pizza(100,'fuck you')

# part_6.3 使用as给函数指定别名
# from 文件名 import 函数名 as 指定别名

from pizza import make_pizza as fuck

fuck(999,'吃屎吧')
fuck(1000,'啊啊啊啊啊','尼玛')

# part_6.4 使用as给模块指定别名

import pizza as p

p.make_pizza(233333,'吃屁吧')
p.make_pizza(199999,'以前不学现在学','mdzz')

# part_6.5 导入模块中的所有函数
# 使用星号* 可导入模块中的所有函数

from pizza import *

make_pizza(100000,'哎')
make_pizza(200000,'奥')



# coding=gbk
# 函数练习6 使用各种方法导入函数

# part_1 格式:import module_name
import show_printed_model

m = ['a','r','y']
show_printed_model.show_printed_models(m)


# part_2 格式:from module_name import function_name
from show_printed_model import show_printed_models

show_printed_models(m)

# part_3 格式: from module_name import function_name as fn

from show_printed_model import show_printed_models as fn

fn(m)

# part_4 格式:import module_name as p

import show_printed_model as p

p.show_printed_models(m)

# part_5 格式: from module_name import *

from show_printed_model import *

show_printed_models(m)

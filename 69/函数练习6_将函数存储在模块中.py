# coding=gbk
# ������ϰ6 ʹ�ø��ַ������뺯��

# part_1 ��ʽ:import module_name
import show_printed_model

m = ['a','r','y']
show_printed_model.show_printed_models(m)


# part_2 ��ʽ:from module_name import function_name
from show_printed_model import show_printed_models

show_printed_models(m)

# part_3 ��ʽ: from module_name import function_name as fn

from show_printed_model import show_printed_models as fn

fn(m)

# part_4 ��ʽ:import module_name as p

import show_printed_model as p

p.show_printed_models(m)

# part_5 ��ʽ: from module_name import *

from show_printed_model import *

show_printed_models(m)

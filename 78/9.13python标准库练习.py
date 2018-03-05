# coding=gbk
# Python标准库

# 练习9.13 使用OrderedDict 从模块collections
from collections import OrderedDict

编程词汇 = OrderedDict()

编程词汇['字符串'] = '由字符,下划线,字母组成的一串字符'
编程词汇['列表'] = '由一系列具有一定排序顺序的元素组成'
编程词汇['元组'] = '不可修改的列表'
编程词汇['字典'] = '键_值对'

for k,v in 编程词汇.items():
    print(k,":",v)

print("\n")

# 练习9.14 使用randint()函数 从模块random
"""创建一个Die类模拟骰子"""
from random import randint

class Die():
    """模拟骰子"""
    
    def __init__(self, side=6):
        """骰子有六面"""
        self.side = side
        
    def roll_die(self):
        """方法 模拟投掷骰子"""
        return randint(1,self.side)
        
die = Die()

results_1 = []
results_2 = []
results_3 = []

for roll_num in range(10):
    result = die.roll_die()
    results_1.append(result)

print(results_1)

die.side = 10
for roll_num in range(10):
    result = die.roll_die()
    results_2.append(result)
    
print(results_2)

die.side = 20
for roll_num in range(10):
    result = die.roll_die()
    results_3.append(result)
    
print(results_3 )

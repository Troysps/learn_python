# coding=gbk
# Python��׼��

# ��ϰ9.13 ʹ��OrderedDict ��ģ��collections
from collections import OrderedDict

��̴ʻ� = OrderedDict()

��̴ʻ�['�ַ���'] = '���ַ�,�»���,��ĸ��ɵ�һ���ַ�'
��̴ʻ�['�б�'] = '��һϵ�о���һ������˳���Ԫ�����'
��̴ʻ�['Ԫ��'] = '�����޸ĵ��б�'
��̴ʻ�['�ֵ�'] = '��_ֵ��'

for k,v in ��̴ʻ�.items():
    print(k,":",v)

print("\n")

# ��ϰ9.14 ʹ��randint()���� ��ģ��random
"""����һ��Die��ģ������"""
from random import randint

class Die():
    """ģ������"""
    
    def __init__(self, side=6):
        """����������"""
        self.side = side
        
    def roll_die(self):
        """���� ģ��Ͷ������"""
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

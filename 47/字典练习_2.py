# coding=gbk
# part_1 将字典练习1中的一系列print语句替换为遍历字典中的键和值的循环
sikan_information = {'frist_name':'chen',
    'slast_name':'sikan',
    'age':21,
    'city':'guangzhou'
        }

for sikan,information in sorted(sikan_information.items()):
    print(sikan+" : "+str(information))

print("\n")
cute_number = {'python':1,
    'java':2,
    'c':3,
    'html':4,
    'php':5
    }

for language in sorted(cute_number.keys()):
    print(language)
    
print("\n")
编程词汇 = {'字符串':'由数字、字母、下划线组成的一串字符',
    '列表':'由一系列特定顺序排列的元素组成',
    '元组':'不可修改的列表',
    '字典':'一系列键_值对',
    '编程基本结构':'语句、方法、函数、关键字',
        }
        
for n,meaning in 编程词汇.items():
    print(n+" : "+meaning+".")
print("\n")

编程词汇['集合'] = '用函数set()表示将一个列表中独一无二的元素提取出来可做另一列表'
编程词汇['函数sorted()'] = '将列表元素按字母顺序进行排序'
编程词汇['for循环'] = '遍历列表中的每个元素 对其执行相同的操作'
编程词汇['if语句'] = '基于条件测试 只有一个测试和一个操作'
编程词汇['布尔表达式'] = '就是条件测试'
print(编程词汇)
print("\n")
for n,m in 编程词汇.items():
    print(n+" : "+m)

print("\n")
# part_2 遍历字典中的键值对 键 值
river_country = {'changjiang' : 'china',
    'huanghe' : 'chian',
    'nile' : 'egypt',
    }
    
for river,country in river_country.items():
    print("The "+river.title()+" runs through "+country.title()+".")
    print(river.title())
    print(country.title())

print("\n")    
# part_3 遍历字典结合if语句
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
    
people = ['jen','phil']
for man in favorite_languages.keys():
    if man in people:
        print(man.title()+" , Thank you for your help!")
    else:
        print("Help me! "+man.title())

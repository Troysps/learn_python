# coding=gbk
# 字典练习3

# part_1 列表中存储字典
sikan_information = {
    'first_name':'chen',
    'last_name':'sikan',
    'age':21,
    'city':'guangzhou'
        }
tianfu_information = {
    'first_name' : 'lei',
    'last_name' : 'tianfu',
    'age' : 21,
    'city' : 'shenzhen',
    }
xifu_information = {
    'first_name' : 'huang',
    'last_name' : 'chenhong',
    'age' : 21,
    'city' : 'zhongshan',
    }
people = [sikan_information,tianfu_information,xifu_information]

for people in people:
    print(people)

# 遍历列表 创建多个列表
dog = {
    'type' : 'chihua hua',
    'master' : 'ten',
    }
cat = {
    'type' : 'lihua',
    'master' : 'lei',
    }
pets = [dog,cat]
for pet in pets:
    print(pets)
        
# part_2字典存储列表
favorite_place = {
    'ten' : ['changsha','hengyang'],
    'lei' : ['shenzheng','beijing'],
    'xifu' : ['shijiegedi'],
    }
for who,where in favorite_place.items():
    print("\n"+who+" favorite place is : ")
    for where in where:
        print("\t"+where.title())

# 字典列表
favorite_number = {
    'ying' : [1,2,3],
    'wo' : [66,99],
    'ta' : [88],
    }
for m,n in favorite_number.items():
    print("\n"+m.title()+"'s favorite number is : ")
    for n in n:
        print(str(n))

# part_3 字典储存字典
cities = {
    'shanghai' : {
        'country' : 'china',
        'populatin' : '30000000',
        'fact' : 'financial centre',
        },
    'beijing' : {
        'country' : 'china',
        'population' : '29000000',
        'fact' : 'political cntre',
        },
    'shenzheng' : {
        'country' : 'china',
        'population' : '300000000',
        'fact' : 'fast developing',
            },
    }
for k,v in cities.items():
    print("\n"+k.title()+":")
    for x,y in v.items():
        print("\t"+x+" : "+str(y))
    
    
    
    
    

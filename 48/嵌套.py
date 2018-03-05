# coding=gbk
# 嵌套 将一系列字典存储在列表中 或将列表作为值存储在字典中
# 列表中存储字典 字典中存储列表 字典中存储字典
# part_1 列表中存储字典
alien_0 = {'color' : 'green','points' : 5}
alien_1 = {'color' : 'yellow','points' : 10}
alien_2 = {'color' : 'red','point' : 15}

aliens = [alien_0,alien_1,alien_2]
print(str(aliens)+"\n")

for alien in aliens:
    print(str(alien))
print("\n")
# 小细节输出数字的时候 多用函数str()

# 小练习：创建一个储存外星人的列表 30个绿色的 5分 低速外星人
aliens = []
for alien in range(0,30):
    new_alien = {'color' : 'green',
        'point' : 5,
        'speed' : 'slow',
        }
    aliens.append(new_alien)
print(str(aliens)+"\n")
# 创建空列表并且充填
# 现在显示前五个这种外星人
for alien in aliens[0:5]:
    print(alien)
print("...")
# 显示创建了多少外星人
print("Total number of aliens : "+str(len(aliens)))
print("\n")

# 小练习：如何处理成群结队的外星人  
for alien in range(0,30):
    new_alien = {'color' : 'green',
        'point' : 5,
        'speed' : 'slow',
        }
    aliens.append(new_alien)
# 下来应用for循环if语句将列表的前三个外星人区别开来
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
print("\n")
# 使用到了for循环 if语句 遍历列表 遍历切片 函数range() str() 方法append()
# 还可以使用if_elif代码块
# 小练习尝试修改
for alien in range(0,30):
    new_alien = {'color' : 'green',
        'point' : 5,
        'speed' : 'slow',
        }
    aliens.append(new_alien)
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = '15'
        alien['speed'] = 'fast'
for alien in aliens[:10]:
    print(alien)

print("\n")

# 这里要将输出结果与上面的结合来看执行一次之后就不执行了if语句特点

# part_2在字典中存储列表 也就是字典中的键对应多个值时使用
pizza = {'crust' : 'thick',
    'topping' : ['mushroom','extra cheese']
    }
# 概述所点的pizza
print("You ordered a "+pizza['crust']+"-crust pizza "
    +"with the following toppings:")
for topping in pizza['topping']:
    print(topping)
# 小练习：有些人喜欢多种语言
favorite_language = {
    'ten' : ['java','c'],
    'troy' : ['python','java'],
    'phil' : ['ruby','php'],
    'edward'   : ['ruby'],
    }

for name,language in favorite_language.items():
    print("\n"+name.title()+"'s favorite languages are :")
    for language in language:
        print("\t"+language.title())

# Part_3 在字典中存储字典 键键值！
user = {
    'aeinstein': {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for n,m in user.items():
    print("\nusername :"+n)
    full_name = m['first']+m['last']
    location = m['location']
    
    print("\tFull name : "+full_name.title())
    print("\tLocation : "+location.title())


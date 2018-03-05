# coding=gbk
# 遍历字典

# part1 遍历所有的键-值对 方法items() 注意返回顺序和储存顺序是不一样的
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# part2 遍历字典所有的键 方法keys() 
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for name in sorted(favorite_languages.keys()):
    print("\n"+name)
print("\n")    
# part3 遍历字典所有的值 方法values() 提取列表中的所有元素 所以有重复
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
    
for language in favorite_languages.values():
    print(language)

print("\n")
# 使用函数set() 在列表中找出独一无二的元素 创建集合 
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for language in set(favorite_languages.values()):
    print(language)    
    
print("\n")
# 测试函数set() 是否对字典的键作用一样 找出独一无二的键  测试通过作用一样 
favorite_languages = {
    'jen':'python',
    'jen':'c',
    'edward':'ruby',
    'phil':'python',
    }
for people in set(favorite_languages.keys()):
    print(people)

print("\n")
# 测试函数set() 遍历字典的键值会怎么样 无效果 并且每次返回顺序是随机的 和存储顺序无关
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for people,language in set(favorite_languages.items()):
    print(people+" : "+language) 

print("\n")
# 测试函数set() 遍历列表   顺序排列函数sorted()可行
alberts = ['a','b','c','a']
for n in sorted(set(alberts)):
    print(n)
    
print("\n")
# 按顺序遍历字典所以的键_值对 函数sorted()  同样可以排列键 值  还有方法reverse()
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }

for key,value in sorted(user_0.items()):
    print(key+" : "+value)

# 经过测试 要注意set() 可以应用在字典的键或值中 以及列表中
# 排列顺序目前是函数sorted() 方法sort() 以及 方法reverse()不可用
print("\n")
# 小练习 字典和列表混用
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

friends = ['jen','sarah']
for name in favorite_languages:
    print(name.title()+" favorite language is "+favorite_languages[name]+".")
    
    if name in friends:
        print(name.title())

print("\n")

# 尝试改变结构 不同在于之前的可以指定符合列表的对象单独发出指令！！！后者不行 前者是全集 后者是不相交的子集
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

friends = ['jen','sarah']
for name in favorite_languages:
    if name in friends:
        print(name.title())
    else:
        print(name.title()+" favorite language is "+favorite_languages[name]+".")


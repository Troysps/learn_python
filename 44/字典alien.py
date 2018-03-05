# coding=gbk
# 字典

# 一个简单字典
alien_0 = {'color':'green','point':5}

print(alien_0['color'])
print(alien_0['point'])
print("\n")
# 访问字典中的值 指定字典名 放在方括号的键
alien_0 = {'color':'green','point':5}
new_alien = alien_0['color']
print("You just killed "+new_alien+" alien.")
# 这里使用了变量储存字典中的值
print("\n")

# 添加键_值对 依次指定字典名 用方括号括起的键和相关联的值
alien_0 = {'color':'green','point':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n")

# 先创建一个空字典
alien_0 = {}

alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)
print("\n")
# 修改字典中的值
alien_0 = {"color":"green"}
print(alien_0)
alien_0['color'] = "yellow"
print(alien_0)
print("\n")
# 删除键_值对
alien_0 = {'color':'green','point':5}
del alien_0['color']
print(alien_0)
print("\n")
# 由类似对象组成的字典
favorite_languages = {
    'jen':'java',
    'yunten':'java',
    'tianfu':'python',
    'phil':'c',
    }
    
print("Tianfu's favorite language is "+favorite_languages['tianfu'].title()+".")
print("\n")
# 趣味练习 修改外星人的速度 从而移动位置
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position :"+str(alien_0['x_position']))

# 向右移动外星人
# 根据外星人的速度移动距离
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度一定很快
    x_increment = 3
    
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("Now x-position : "+str(alien_0['x_position']))

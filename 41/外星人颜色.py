# coding=gbk
# ��������ɫ_1 ��if���(�����汾 һ��ͨ���� һ��ûͨ����
alien_color = ['green','yellow','red']
color = 'green'
if color == 'green':
    print("Player get 5 points!")
if color != 'green':
    print("Player get 10 points!")
print("\n")
# ��������ɫ_2 if_else�ṹ(�����汾 һ��������ɫ һ��û��)
alien_color = ['green','yellow','red']
color = 'green'
if color == 'green':
    print("Player get 5 points!")
else:
    print("Player get 10 points!")
print("\n")
for color in alien_color:
    if color == 'green':
        print("Player get 5 points!")
    else:
        print("Player get 10 points!")
print("\n")
# ��������ɫ_3 if_elif_else�ṹ
alien_color = ['green','yellow','red']
color = 'red'
if color == 'green':
    print("Player get 5 points.")
elif color == 'yellow':
    print("Player get 10 points.")
else:
    print("Player get 15 points.")
print("\n")
# �汾2
color = 'yellow'
if color == 'green':
    print("Player get 5 points.")
elif color == 'yellow':
    print("Player get 10 points.")
else:
    print("Player get 15 points.")
alien_color = ['green','yellow','red']
print("\n")
# �汾3
color = 'green'
if color == 'green':
    print("Player get 5 points.")
elif color == 'yellow':
    print("Player get 10 points.")
else:
    print("Player get 15 points.")
alien_color = ['green','yellow','red']
print("\n")
# ����
for color in alien_color:
    if color == 'green':
        print("Player get 5 points.")
    elif color == 'yellow':
        print("Player get 10 points.")
    else:
        print("Player get 15 points.")
# �����Ĳ�ͬ�׶�
print("\n")
age = 21
if age < 2:
    print("You are a baby.")
elif (age >= 2) and (age < 4):
    print("You are learning walk!")
elif (age >= 4) and (age < 13):
    print("You are a child.")
elif (age >= 13) and (age < 20):
    print("You are a teenager.")
elif (age >= 20) and (age < 65 ):
    print("You are an adult.")
elif age >= 65:
    print("You are an old man.")
print("\n")
# ϲ����ˮ��
favorite_fruit = ['banana','apple','cucumber','peach','durian']
if 'banana' in favorite_fruit:
    print("U really like bananas.")
if 'apple' in favorite_fruit:
    print("U really like apples.")
if 'pizza' in favorite_fruit:
    print("U really like cucumber")
if 'peach' in favorite_fruit:
    print("U really like peaches.")
if 'dragon fruit' in favorite_fruit:
    print("U really like durian.")

# coding=gbk
# ����������ϰ
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru'+"\n")
print("\n")
age = 19
print(age > 20)
print(age < 20)
print(age >= 18)
print(age <= 8)
print(age != 20)
print(age != 19)
print("\n")
menus=['rice','meat','beef','pizza']
print('fruit' in menus)
print('fruit' not in menus)
print(menus[0] != 'meat')
print(menus[-1] == 'pizza')
print(menus[2:] == ('beef' and 'pizza'))
print(menus[2:] == ('beef' or 'pizza'))
# ���һ�������pizza!!!!˵����������Ƿֿ����ģ�and���ſ� or�Ƿֿ� �����ַ���(����)
print(menus[2:])
print("\n")
# �������������
car_1 = 'bmw'
car_2 = 'Bmw'
print(car_1 == car_2)
print(car_1.title() == car_2)
print(car_1 == car_2.lower())
n_1 = 2
n_2 = 10
print(n_1 > n_2)
print(n_1 >= n_2)
print(n_1 == n_2)
print(n_1 != n_2)
print(n_1 < n_2)
print(n_1 <= n_2)

print((n_1 > 1) and (n_1 <= 3))
print((n_2 < 8) or (n_2 >= 8))

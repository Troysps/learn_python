# coding=gbk
# 条件测试练习
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
# 最后一个输出了pizza!!!!说明输出里面是分开看的！and连着看 or是分开 两个字符串(括号)
print(menus[2:])
print("\n")
# 更多的条件测试
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

# coding=gbk

# 9.4.2 ��һ��ģ���д洢�����

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n")
# 9.4.3 ��һ��ģ���е�������

from car import Car,ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

print("\n")
# 9.4.4 ��������ģ��
import car

my_beetle = Car('volkswageng', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 9.4.5 ����ģ���е������� from module_name import *



# coding=gbk

# 9.4.2 在一个模块中存储多个类

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n")
# 9.4.3 在一个模块中导入多个类

from car import Car,ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

print("\n")
# 9.4.4 导入整个模块
import car

my_beetle = Car('volkswageng', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 9.4.5 导入模块中的所有类 from module_name import *



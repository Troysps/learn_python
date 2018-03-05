# coding=gbk
# 使用类和实例 
# 三个部分:1.在类中方法是用return语句返回值——用来汇总信息
#         2.给属性指定默认值
#         3.修改属性的值 直接修改 方法设置修改 通过方法进行递增

# 9.2.1 在类中方法使用return语句返回值——汇总属性信息
class Car():
    """创建一个 汽车类"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的信息"""
        self.make = make
        self.model = model
        self.year = str(year)
        
    def get_descriptive_name(self):
        """返回整洁完全的汽车姓名"""
        long_name = self.year + " " + self.make + " " + self.model
        return long_name.title()
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print("\n")

# 9.2.2 给属性指定默认值 在类中的特殊方法中给属性指定默认值 那么无需为它提供初始值的形参
class Car():
    """创建一个 汽车类"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的信息"""
        self.make = make
        self.model = model
        self.year = str(year)
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """方法一 返回整洁完全的汽车名"""
        long_name = self.year + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """方法二 指出汽车的行驶里程碑"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("\n")

# 9.2.3 修改属性的值 三种方式 
# 1.通过实例修改 直接修改法
# 2.通过方法修改 常用的修改属性方法 用于更新属性
# 3.通过方法对属性的值进行递增

# 1.直接修改
my_new_car.odometer_reading = 233
my_new_car.read_odometer()
print("\n")

# 2.通过方法修改属性的值 这是Python中常用的方法 用于更新属性
class Car():
    """创建一个 汽车类"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的信息"""
        self.make = make
        self.model = model
        self.year = str(year)
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """方法一 返回整洁完全的汽车名"""
        long_name = self.year + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """方法二 指出汽车的行驶里程碑"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """方法三 将里程表读数设置为指定的值"""
        self.odometer_reading = mileage
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
print("\n")

# 可以对方法三 进行扩展 禁止任何人将里程表读数往回溯
class Car():
    """创建一个 汽车类"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的信息"""
        self.make = make
        self.model = model
        self.year = str(year)
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """方法一 返回整洁完全的汽车名"""
        long_name = self.year + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """方法二 指出汽车的行驶里程碑"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """
        将历程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_read = mileage
        else:
            print("You can't roll back an odometer!")
            

# 3.通过方法对属性的值进行增递
class Car():
    """创建一个 汽车类"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的信息"""
        self.make = make
        self.model = model
        self.year = str(year)
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """方法一 返回整洁完全的汽车名"""
        long_name = self.year + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """方法二 指出汽车的行驶里程碑"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """
        方法三
        将历程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        """方法四 将里程表读数增加指定的量"""
        self.odometer_reading += miles
        
        
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(1000)
my_used_car.read_odometer()

my_used_car.increment_odometer(10000)
my_used_car.read_odometer()

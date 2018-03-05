# coding=gbk
# 9.3_继承 一个类继承另一个类时 自动获得另一个类的所有属性和方法
#         原有的类为父类 新类称为子类 继承的同时还可以定义自己的属性和方法

# 9.3.1 子类的方法__init__()接受创建父类实例所需的信息
class Car():
    """创建一个汽车的类"""
    
    def __init__(self, make, model, year):
        """
        方法一 永远是特殊的方法
        格式化汽车类的厂商 型号 年份
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """方法二 使用return语句返回值 汇总信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name
        
    def read_odometer(self):
        """方法三 读取汽车运行的里程表数值"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """方法四 通过方法更新里程表的数值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        """方法五 通过方法递增里程表数值"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """方法六 汽车油箱"""
        print("About 100L")
        
# 以上是父类 下面创建子类
class ElectricCar(Car):
    """创建汽车下面的一个子类 电动汽车类"""
    
    def __init__(self, make, model, year):
        """方法一 特殊方法初始化父类的属性使子类接受创建父类实例所需的信息"""
        super().__init__(make, model, year)
        # 使用super()特殊函数 使子类调用父类的方法 也包含父类的所有属性
        

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


# 9.3.3 给子类定义属性和方法
class ElectricCar(Car):
    """创建汽车下面的一个子类 电动汽车类"""
    
    def __init__(self, make, model, year):
        """
        方法一 特殊方法初始化父类的属性使子类接受创建父类实例所需的信息
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        # 在特殊函数super()之下添加电动汽车的特有属性
        
    def describe_battery(self):
        """子类的方法一 打印一条描述电瓶容量的消息"""
        print("This car has a",str(self.battery_size),"-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 9.3.4 重写父类的方法
class ElectricCar(Car):
    """创建汽车下面的一个子类 电动汽车类"""
    
    def __init__(self, make, model, year):
        """
        方法一 特殊方法初始化父类的属性使子类接受创建父类实例所需的信息
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        # 在特殊函数super()之下添加电动汽车的特有属性
        
    def describe_battery(self):
        """子类的方法一 打印一条描述电瓶容量的消息"""
        print("This car has a",str(self.battery_size),"-kWh battery.")
        
    def fill_gas_tank(self):
        """子类的方法二 电动汽车没有油箱"""
        print("This car doesn't need a gas tank")

print("\n")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
print("\n")

# 9.3.4 将实例用作属性 将大类拆分成多个协同一致的小类
class Car():
    """创建一个汽车的类"""
    
    def __init__(self, make, model, year):
        """
        方法一 永远是特殊的方法
        格式化汽车类的厂商 型号 年份
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """方法二 使用return语句返回值 汇总信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name
        
    def read_odometer(self):
        """方法三 读取汽车运行的里程表数值"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """方法四 通过方法更新里程表的数值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        """方法五 通过方法递增里程表数值"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """方法六 汽车油箱"""
        print("About 100L")
        
class Battery():
    """分出一个电动汽车的电瓶的小类"""
    
    def __init__(self, battery_size=70):
        """特殊方法一 初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """方法二 打印一条描述电瓶容量的消息"""
        print("This car has a",str(self.battery_size),"-kWh battery.")
        
    def get_range(self):
        """方法三 打印一条消息 指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can approximately " + str(range)
        message += " miles on a full charge"
        print(message)
        
class ElectricCar(Car):
    """继承汽车父类 并且有独特之处的电动汽车"""
    
    def __init__(self, make, model, year):
        """
        初始化父类属性 在初始化子类的特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

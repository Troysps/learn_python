# coding=gbk
"""一组用于表示电动汽车的类"""

# 9.4.6 在一个模块中导入另一个模块
from car import Car


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




my_beetle = Car('volkswageng', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

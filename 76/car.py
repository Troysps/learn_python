# coding=gbk
# 9.4 导入类
"""一组用于表示汽车的类"""
# 创建只有一个类的单独文件
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
        
        
# 在模块中创建多个类
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
        
        
        

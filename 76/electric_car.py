# coding=gbk
"""һ�����ڱ�ʾ�綯��������"""

# 9.4.6 ��һ��ģ���е�����һ��ģ��
from car import Car


class Battery():
    """�ֳ�һ���綯�����ĵ�ƿ��С��"""
    
    def __init__(self, battery_size=70):
        """���ⷽ��һ ��ʼ����ƿ������"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """������ ��ӡһ��������ƿ��������Ϣ"""
        print("This car has a",str(self.battery_size),"-kWh battery.")
        
    def get_range(self):
        """������ ��ӡһ����Ϣ ָ����ƿ���������"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can approximately " + str(range)
        message += " miles on a full charge"
        print(message)
        
class ElectricCar(Car):
    """�̳��������� �����ж���֮���ĵ綯����"""
    
    def __init__(self, make, model, year):
        """
        ��ʼ���������� �ڳ�ʼ����������е�����
        """
        super().__init__(make, model, year)
        self.battery = Battery()




my_beetle = Car('volkswageng', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

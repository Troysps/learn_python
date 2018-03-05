# coding=gbk
# 9.3_�̳� һ����̳���һ����ʱ �Զ������һ������������Ժͷ���
#         ԭ�е���Ϊ���� �����Ϊ���� �̳е�ͬʱ�����Զ����Լ������Ժͷ���

# 9.3.1 ����ķ���__init__()���ܴ�������ʵ���������Ϣ
class Car():
    """����һ����������"""
    
    def __init__(self, make, model, year):
        """
        ����һ ��Զ������ķ���
        ��ʽ��������ĳ��� �ͺ� ���
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """������ ʹ��return��䷵��ֵ ������Ϣ"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name
        
    def read_odometer(self):
        """������ ��ȡ�������е���̱���ֵ"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """������ ͨ������������̱����ֵ"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        """������ ͨ������������̱���ֵ"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """������ ��������"""
        print("About 100L")
        
# �����Ǹ��� ���洴������
class ElectricCar(Car):
    """�������������һ������ �綯������"""
    
    def __init__(self, make, model, year):
        """����һ ���ⷽ����ʼ�����������ʹ������ܴ�������ʵ���������Ϣ"""
        super().__init__(make, model, year)
        # ʹ��super()���⺯�� ʹ������ø���ķ��� Ҳ�����������������
        

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


# 9.3.3 �����ඨ�����Ժͷ���
class ElectricCar(Car):
    """�������������һ������ �綯������"""
    
    def __init__(self, make, model, year):
        """
        ����һ ���ⷽ����ʼ�����������ʹ������ܴ�������ʵ���������Ϣ
        �ٳ�ʼ���綯�������е�����
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        # �����⺯��super()֮����ӵ綯��������������
        
    def describe_battery(self):
        """����ķ���һ ��ӡһ��������ƿ��������Ϣ"""
        print("This car has a",str(self.battery_size),"-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 9.3.4 ��д����ķ���
class ElectricCar(Car):
    """�������������һ������ �綯������"""
    
    def __init__(self, make, model, year):
        """
        ����һ ���ⷽ����ʼ�����������ʹ������ܴ�������ʵ���������Ϣ
        �ٳ�ʼ���綯�������е�����
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        # �����⺯��super()֮����ӵ綯��������������
        
    def describe_battery(self):
        """����ķ���һ ��ӡһ��������ƿ��������Ϣ"""
        print("This car has a",str(self.battery_size),"-kWh battery.")
        
    def fill_gas_tank(self):
        """����ķ����� �綯����û������"""
        print("This car doesn't need a gas tank")

print("\n")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
print("\n")

# 9.3.4 ��ʵ���������� �������ֳɶ��Эͬһ�µ�С��
class Car():
    """����һ����������"""
    
    def __init__(self, make, model, year):
        """
        ����һ ��Զ������ķ���
        ��ʽ��������ĳ��� �ͺ� ���
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """������ ʹ��return��䷵��ֵ ������Ϣ"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name
        
    def read_odometer(self):
        """������ ��ȡ�������е���̱���ֵ"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """������ ͨ������������̱����ֵ"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        """������ ͨ������������̱���ֵ"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """������ ��������"""
        print("About 100L")
        
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
        
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

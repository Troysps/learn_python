# coding=gbk
# ʹ�����ʵ�� 
# ��������:1.�����з�������return��䷵��ֵ��������������Ϣ
#         2.������ָ��Ĭ��ֵ
#         3.�޸����Ե�ֵ ֱ���޸� ���������޸� ͨ���������е���

# 9.2.1 �����з���ʹ��return��䷵��ֵ��������������Ϣ
class Car():
    """����һ�� ������"""
    
    def __init__(self, make, model, year):
        """��ʼ��������������Ϣ"""
        self.make = make
        self.model = model
        self.year = str(year)
        
    def get_descriptive_name(self):
        """����������ȫ����������"""
        long_name = self.year + " " + self.make + " " + self.model
        return long_name.title()
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
print("\n")

# 9.2.2 ������ָ��Ĭ��ֵ �����е����ⷽ���и�����ָ��Ĭ��ֵ ��ô����Ϊ���ṩ��ʼֵ���β�
class Car():
    """����һ�� ������"""
    
    def __init__(self, make, model, year):
        """��ʼ��������������Ϣ"""
        self.make = make
        self.model = model
        self.year = str(year)
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """����һ ����������ȫ��������"""
        long_name = self.year + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """������ ָ����������ʻ��̱�"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("\n")

# 9.2.3 �޸����Ե�ֵ ���ַ�ʽ 
# 1.ͨ��ʵ���޸� ֱ���޸ķ�
# 2.ͨ�������޸� ���õ��޸����Է��� ���ڸ�������
# 3.ͨ�����������Ե�ֵ���е���

# 1.ֱ���޸�
my_new_car.odometer_reading = 233
my_new_car.read_odometer()
print("\n")

# 2.ͨ�������޸����Ե�ֵ ����Python�г��õķ��� ���ڸ�������
class Car():
    """����һ�� ������"""
    
    def __init__(self, make, model, year):
        """��ʼ��������������Ϣ"""
        self.make = make
        self.model = model
        self.year = str(year)
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """����һ ����������ȫ��������"""
        long_name = self.year + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """������ ָ����������ʻ��̱�"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """������ ����̱��������Ϊָ����ֵ"""
        self.odometer_reading = mileage
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
print("\n")

# ���ԶԷ����� ������չ ��ֹ�κ��˽���̱����������
class Car():
    """����һ�� ������"""
    
    def __init__(self, make, model, year):
        """��ʼ��������������Ϣ"""
        self.make = make
        self.model = model
        self.year = str(year)
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """����һ ����������ȫ��������"""
        long_name = self.year + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """������ ָ����������ʻ��̱�"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """
        �����̱��������Ϊָ����ֵ
        ��ֹ����̱�������ص�
        """
        if mileage >= self.odometer_reading:
            self.odometer_read = mileage
        else:
            print("You can't roll back an odometer!")
            

# 3.ͨ�����������Ե�ֵ��������
class Car():
    """����һ�� ������"""
    
    def __init__(self, make, model, year):
        """��ʼ��������������Ϣ"""
        self.make = make
        self.model = model
        self.year = str(year)
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """����һ ����������ȫ��������"""
        long_name = self.year + " " + self.make + " " +self.model
        return long_name.title()
        
    def read_odometer(self):
        """������ ָ����������ʻ��̱�"""
        print("This car has",str(self.odometer_reading),"miles on it.")
        
    def update_odometer(self,mileage):
        """
        ������
        �����̱��������Ϊָ����ֵ
        ��ֹ����̱�������ص�
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        """������ ����̱��������ָ������"""
        self.odometer_reading += miles
        
        
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(1000)
my_used_car.read_odometer()

my_used_car.increment_odometer(10000)
my_used_car.read_odometer()

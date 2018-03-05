# coding=gbk
# �̳���ϰ

# 9.6 �̳�һ���� ����������������е����� �ͷ���
class Restaurant():
    """����һ����������"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """��ʼ���������ֺ���⿷�ʽ"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """���е�һ������ ��������"""
        print("\n" + self.restaurant_name.title(),"located in Shenzhen.")
        print("Cuisine Type :",self.cuisine_type)
        
    def open_restaurant(self):
        """���е�һ������ ָ����������Ӫҵ"""
        print(self.restaurant_name.title(),"now is opening")
        
class IceCreamStand(Restaurant):
    """�����͹ݵ�һ������ ����ܵ�"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """���ܲ���ʽ�����������"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
        
    def icecream_flavors(self,flavors):
        """���� ��ʾ���ָ����ı���ܿ�ζ"""
        self.flavors.append(flavors)
        print(set(self.flavors))
        
        
ice = IceCreamStand('shanghaojia','icecream')
ice.icecream_flavors('banana')
ice.icecream_flavors('banana')
ice.icecream_flavors('apple')

# ���ﴴ��һ��Ĭ������Ϊ���б��ֵ �ڷ����п��Խ�����Ӹ��ָ����ı���� set������һ�޶�

# 9.7 �����û�������� ����Ա
class User():
    """����һ���û�����"""
    
    def __init__(self,first_name,last_name,gender,age):
        """��ʼ���û������� �Ա� ����"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = str(age)
        # ����Ĭ��ֵ ����Ҫ�����ⷽ��������������β�
        self.login_attempts = 0
        
    def describe_user(self):
        """����һ ��ӡ�û��Ļ�����Ϣ"""
        print("\nUsername:",self.first_name.title()+' '+self.last_name.title())
        print("User Gender:",self.gender)
        print("User age:",self.age)
        
    def greet_user(self):
        """������ ���û��ʺ�"""
        print("Hello,Handsome Boy:",self.first_name.title()+' '+self.last_name.title())
        
    def increment_login_attempts(self):
        """������ ÿʹ��һ�θ÷��� �û����Ե�½�˴���1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """������ ʹ�ø÷��������û���½����"""
        self.login_attempts = 0
        
    def show_attempts(self):
        """������ ��ʾ�û��ĵ�½����"""
        print("\nUser login attempts:",str(self.login_attempts))
        
        
class Admin(User):
    """�����û�������� ����Ա��"""
    
    def __init__(self,first_name, last_name, gender,age):
        """���ܲ���ʼ�����������"""
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ['can add post','can delete post','can ban user']
        
    def admin_privileges(self):
        """���� ˵�������Ȩ��"""
        print("\nThe admin user have these privileges:")
        for n in self.privileges:
            print("\t",n)
    

admin_1 = Admin('lei','tianfu','male',21)
admin_1.admin_privileges()
# ע��forѭ�����б���Ҫ���б��������()

# 9.8 ���û����д���һ��Ȩ��С�� ���͹���Ա����
class User():
    """����һ���û�����"""
    
    def __init__(self,first_name,last_name,gender,age):
        """��ʼ���û������� �Ա� ����"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = str(age)
        # ����Ĭ��ֵ ����Ҫ�����ⷽ��������������β�
        self.login_attempts = 0
        
    def describe_user(self):
        """����һ ��ӡ�û��Ļ�����Ϣ"""
        print("\nUsername:",self.first_name.title()+' '+self.last_name.title())
        print("User Gender:",self.gender)
        print("User age:",self.age)
        
    def greet_user(self):
        """������ ���û��ʺ�"""
        print("Hello,Handsome Boy:",self.first_name.title()+' '+self.last_name.title())
        
    def increment_login_attempts(self):
        """������ ÿʹ��һ�θ÷��� �û����Ե�½�˴���1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """������ ʹ�ø÷��������û���½����"""
        self.login_attempts = 0
        
    def show_attempts(self):
        """������ ��ʾ�û��ĵ�½����"""
        print("\nUser login attempts:",str(self.login_attempts))

class Privileges():
    """����һ���йع���ԱȨ�޵�С��"""
    
    def __init__(
    self,
    privileges= ['can add post','can delete post','can ban user']):
        """��ʼ��Ȩ�޵�����"""
        self.privileges = privileges
        
    def show_privileges(self):
        """���� �����йع���ԱȨ�޵�ְ��"""
        print("\nThe admin user have these privileges:")
        for n in self.privileges:
            print("\t",n)
            
            
class Admin(User):
    """�����û�������� ����Ա��"""
    
    def __init__(self,first_name, last_name, gender,age):
        """���ܲ���ʼ�����������"""
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()
        
        
admin_1 = Admin('lei','tianfu','male',21)
admin_1.privileges.show_privileges()
# �ڸ�С����������ֵ��ʱ�����Ĭ��ֵ �����ⷽ�����������

# 9.9 ��ƿ����ģ��ʵ�� 
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
        
    def upgrade_battery(self):
        """������ ����ƿ����"""
        if self.battery_size != 85:
            self.battery_size = 85
        
class ElectricCar(Car):
    """�̳��������� �����ж���֮���ĵ綯����"""
    
    def __init__(self, make, model, year):
        """
        ��ʼ���������� �ڳ�ʼ����������е�����
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
print("\n")        
a_car = ElectricCar('tesla', 'model s', 2016)
a_car.battery.get_range()
a_car.battery.upgrade_battery()
a_car.battery.get_range()

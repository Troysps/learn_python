# coding=gbk
# 继承练习

# 9.6 继承一个类 并在子类中添加特有的属性 和方法
class Restaurant():
    """创建一个餐厅的类"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐厅名字和烹饪方式"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """类中的一个方法 描述餐厅"""
        print("\n" + self.restaurant_name.title(),"located in Shenzhen.")
        print("Cuisine Type :",self.cuisine_type)
        
    def open_restaurant(self):
        """类中的一个方法 指出餐厅正在营业"""
        print(self.restaurant_name.title(),"now is opening")
        
class IceCreamStand(Restaurant):
    """创建餐馆的一个子类 冰淇淋店"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """接受并格式化父类的属性"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
        
    def icecream_flavors(self,flavors):
        """方法 显示各种各样的冰淇淋口味"""
        self.flavors.append(flavors)
        print(set(self.flavors))
        
        
ice = IceCreamStand('shanghaojia','icecream')
ice.icecream_flavors('banana')
ice.icecream_flavors('banana')
ice.icecream_flavors('apple')

# 这里创建一个默认属性为空列表的值 在方法中可以进行添加各种各样的冰淇淋 set函数独一无二

# 9.7 创建用户类的子类 管理员
class User():
    """创建一个用户的类"""
    
    def __init__(self,first_name,last_name,gender,age):
        """初始化用户的名字 性别 年龄"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = str(age)
        # 设置默认值 不需要再特殊方法的括号中添加形参
        self.login_attempts = 0
        
    def describe_user(self):
        """方法一 打印用户的基本信息"""
        print("\nUsername:",self.first_name.title()+' '+self.last_name.title())
        print("User Gender:",self.gender)
        print("User age:",self.age)
        
    def greet_user(self):
        """方法二 向用户问好"""
        print("Hello,Handsome Boy:",self.first_name.title()+' '+self.last_name.title())
        
    def increment_login_attempts(self):
        """方法三 每使用一次该方法 用户尝试登陆此处加1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """方法四 使用该方法重置用户登陆次数"""
        self.login_attempts = 0
        
    def show_attempts(self):
        """方法五 显示用户的登陆次数"""
        print("\nUser login attempts:",str(self.login_attempts))
        
        
class Admin(User):
    """创建用户类的子类 管理员类"""
    
    def __init__(self,first_name, last_name, gender,age):
        """接受并初始化父类的属性"""
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ['can add post','can delete post','can ban user']
        
    def admin_privileges(self):
        """方法 说明管理的权限"""
        print("\nThe admin user have these privileges:")
        for n in self.privileges:
            print("\t",n)
    

admin_1 = Admin('lei','tianfu','male',21)
admin_1.admin_privileges()
# 注意for循环加列表不需要在列表名后面加()

# 9.8 在用户类中创建一个权限小类 并和管理员关联
class User():
    """创建一个用户的类"""
    
    def __init__(self,first_name,last_name,gender,age):
        """初始化用户的名字 性别 年龄"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = str(age)
        # 设置默认值 不需要再特殊方法的括号中添加形参
        self.login_attempts = 0
        
    def describe_user(self):
        """方法一 打印用户的基本信息"""
        print("\nUsername:",self.first_name.title()+' '+self.last_name.title())
        print("User Gender:",self.gender)
        print("User age:",self.age)
        
    def greet_user(self):
        """方法二 向用户问好"""
        print("Hello,Handsome Boy:",self.first_name.title()+' '+self.last_name.title())
        
    def increment_login_attempts(self):
        """方法三 每使用一次该方法 用户尝试登陆此处加1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """方法四 使用该方法重置用户登陆次数"""
        self.login_attempts = 0
        
    def show_attempts(self):
        """方法五 显示用户的登陆次数"""
        print("\nUser login attempts:",str(self.login_attempts))

class Privileges():
    """创建一个有关管理员权限的小类"""
    
    def __init__(
    self,
    privileges= ['can add post','can delete post','can ban user']):
        """初始化权限的属性"""
        self.privileges = privileges
        
    def show_privileges(self):
        """方法 描述有关管理员权限的职能"""
        print("\nThe admin user have these privileges:")
        for n in self.privileges:
            print("\t",n)
            
            
class Admin(User):
    """创建用户类的子类 管理员类"""
    
    def __init__(self,first_name, last_name, gender,age):
        """接受并初始化父类的属性"""
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()
        
        
admin_1 = Admin('lei','tianfu','male',21)
admin_1.privileges.show_privileges()
# 在给小类设置属性值的时候添加默认值 在特殊方法括号里添加

# 9.9 电瓶升级模拟实物 
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
        
    def upgrade_battery(self):
        """方法四 检查电瓶容量"""
        if self.battery_size != 85:
            self.battery_size = 85
        
class ElectricCar(Car):
    """继承汽车父类 并且有独特之处的电动汽车"""
    
    def __init__(self, make, model, year):
        """
        初始化父类属性 在初始化子类的特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
print("\n")        
a_car = ElectricCar('tesla', 'model s', 2016)
a_car.battery.get_range()
a_car.battery.upgrade_battery()
a_car.battery.get_range()

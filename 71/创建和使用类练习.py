# coding=gbk
# 9.1-9.3练习 创建和使用类

# 9.1 创建一个类
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
        
i = Restaurant('ji','american cuisine')
print(i.restaurant_name.title(),"is good.")
print("Ten like",i.cuisine_type,".")

i.describe_restaurant()
i.open_restaurant()
print("\n")
# 9.2 创建三个实例
t = Restaurant('lei','chinese cuisine')
h = Restaurant('huang','japan cuisine')
j = Restaurant('hua','korea cuisine')


t.describe_restaurant()
h.describe_restaurant()
j.describe_restaurant()

# 9.3 创建并使用类  名为user的类 包含first_name last_name两个属性以及其他的属性
class User():
    """创建一个用户的类"""
    
    def __init__(self,first_name,last_name,gender,age):
        """初始化用户的名字 性别 年龄"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = str(age)
        
    def describe_user(self):
        """方法一 打印用户的基本信息"""
        print("\nUsername:",self.first_name.title()+' '+self.last_name.title())
        print("User Gender:",self.gender)
        print("User age:",self.age)
        
    def greet_user(self):
        """方法二 向用户问好"""
        print("Hello,Handsome Boy:",self.first_name.title()+' '+self.last_name.title())
        

user_1 = User('lei','tianfu','male',21)
user_1.describe_user()
user_1.greet_user()


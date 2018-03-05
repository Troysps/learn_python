# coding=gbk
# 使用类和实例 练习

# 9.4 在9.1的练习中添加一个默认值 其默认值设置为0 根据这个类创建实例 打印有多少在这用餐
class Restaurant():
    """创建一个餐厅的类"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐厅名字和烹饪方式"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """方法一 描述餐厅"""
        print("\n" + self.restaurant_name.title(),"located in Shenzhen.")
        print("Cuisine Type :",self.cuisine_type)
        
    def open_restaurant(self):
        """方法二 指出餐厅正在营业"""
        print(self.restaurant_name.title(),"now is opening")
    
    def set_number_served(self,set_number):
        """方法三 在类中采用方法修改正在就餐的人数"""
        self.number_served = set_number
        
    
    def increment_number_served(self,number):
        """方法四 在类中采用方法对属性的值进行递增"""
        self.number_served += number
    
    def serving_number(self):
        """方法五 打印有多少人正在用餐"""
        print("\nThe",restaurant.restaurant_name.title(),"have",
        str(restaurant.number_served),"people served today.")
    
restaurant = Restaurant('industrial','chinese')
restaurant.serving_number()
    
restaurant.number_served = 20
# 直接修改用句点法 加上 = 号!!!

restaurant.set_number_served(100)
restaurant.serving_number()

restaurant.increment_number_served(10000)
restaurant.serving_number()

# 通过三种方法修改值 不要嫌弃麻烦 多设置方法 会清晰的多

# 9.5 使用类和实例 通过三种方法修改属性的值 练习2
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
        
user_1 = User('lei','tianfu','male',21)
user_1.show_attempts()

user_1.increment_login_attempts()
user_1.show_attempts()

user_1.increment_login_attempts()
user_1.show_attempts()

user_1.reset_login_attempts()
user_1.show_attempts()

# 加油完美 

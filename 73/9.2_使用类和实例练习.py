# coding=gbk
# ʹ�����ʵ�� ��ϰ

# 9.4 ��9.1����ϰ�����һ��Ĭ��ֵ ��Ĭ��ֵ����Ϊ0 ��������ഴ��ʵ�� ��ӡ�ж��������ò�
class Restaurant():
    """����һ����������"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """��ʼ���������ֺ���⿷�ʽ"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """����һ ��������"""
        print("\n" + self.restaurant_name.title(),"located in Shenzhen.")
        print("Cuisine Type :",self.cuisine_type)
        
    def open_restaurant(self):
        """������ ָ����������Ӫҵ"""
        print(self.restaurant_name.title(),"now is opening")
    
    def set_number_served(self,set_number):
        """������ �����в��÷����޸����ھͲ͵�����"""
        self.number_served = set_number
        
    
    def increment_number_served(self,number):
        """������ �����в��÷��������Ե�ֵ���е���"""
        self.number_served += number
    
    def serving_number(self):
        """������ ��ӡ�ж����������ò�"""
        print("\nThe",restaurant.restaurant_name.title(),"have",
        str(restaurant.number_served),"people served today.")
    
restaurant = Restaurant('industrial','chinese')
restaurant.serving_number()
    
restaurant.number_served = 20
# ֱ���޸��þ�㷨 ���� = ��!!!

restaurant.set_number_served(100)
restaurant.serving_number()

restaurant.increment_number_served(10000)
restaurant.serving_number()

# ͨ�����ַ����޸�ֵ ��Ҫ�����鷳 �����÷��� �������Ķ�

# 9.5 ʹ�����ʵ�� ͨ�����ַ����޸����Ե�ֵ ��ϰ2
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
        
user_1 = User('lei','tianfu','male',21)
user_1.show_attempts()

user_1.increment_login_attempts()
user_1.show_attempts()

user_1.increment_login_attempts()
user_1.show_attempts()

user_1.reset_login_attempts()
user_1.show_attempts()

# �������� 

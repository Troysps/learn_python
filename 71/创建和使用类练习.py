# coding=gbk
# 9.1-9.3��ϰ ������ʹ����

# 9.1 ����һ����
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
        
i = Restaurant('ji','american cuisine')
print(i.restaurant_name.title(),"is good.")
print("Ten like",i.cuisine_type,".")

i.describe_restaurant()
i.open_restaurant()
print("\n")
# 9.2 ��������ʵ��
t = Restaurant('lei','chinese cuisine')
h = Restaurant('huang','japan cuisine')
j = Restaurant('hua','korea cuisine')


t.describe_restaurant()
h.describe_restaurant()
j.describe_restaurant()

# 9.3 ������ʹ����  ��Ϊuser���� ����first_name last_name���������Լ�����������
class User():
    """����һ���û�����"""
    
    def __init__(self,first_name,last_name,gender,age):
        """��ʼ���û������� �Ա� ����"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = str(age)
        
    def describe_user(self):
        """����һ ��ӡ�û��Ļ�����Ϣ"""
        print("\nUsername:",self.first_name.title()+' '+self.last_name.title())
        print("User Gender:",self.gender)
        print("User age:",self.age)
        
    def greet_user(self):
        """������ ���û��ʺ�"""
        print("Hello,Handsome Boy:",self.first_name.title()+' '+self.last_name.title())
        

user_1 = User('lei','tianfu','male',21)
user_1.describe_user()
user_1.greet_user()


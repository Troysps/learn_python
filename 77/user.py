# coding=gbk
# 9.12 ��������ϰ ���ģ��

"""�����û���"""

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

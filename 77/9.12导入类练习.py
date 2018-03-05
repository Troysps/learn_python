# coding=gbk
# 9.12 ��������ϰ ���ģ��

"""��admin privileges���е����û�ģ���е�user��"""
from user import User


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
        
        
user_1 = Admin('lei', 'tianfu', 'male', 21)
user_1.privileges.show_privileges()
user_1.describe_user()

# coding=gbk
# 9.12 导入类练习 多个模块

"""在admin privileges类中导入用户模块中的user类"""
from user import User


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
        
        
user_1 = Admin('lei', 'tianfu', 'male', 21)
user_1.privileges.show_privileges()
user_1.describe_user()

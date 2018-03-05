# coding=gbk
# 9.12 导入类练习 多个模块

"""创建用户类"""

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

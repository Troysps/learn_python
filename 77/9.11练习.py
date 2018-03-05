# coding=gbk
# 9.2 导入类的练习 导入Admin类

"""从用户模块中导入 user类 admin类 privilege类"""

from user import User, Admin, Privileges

user_1 = Admin('lei', 'tianfu', 'male', 21)
user_1.privileges.show_privileges()
user_1.describe_user()

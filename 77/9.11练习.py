# coding=gbk
# 9.2 ���������ϰ ����Admin��

"""���û�ģ���е��� user�� admin�� privilege��"""

from user import User, Admin, Privileges

user_1 = Admin('lei', 'tianfu', 'male', 21)
user_1.privileges.show_privileges()
user_1.describe_user()

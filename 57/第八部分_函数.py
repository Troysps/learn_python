# coding=gbk
# ��д����

# part_1 ���庯�� �ؼ���def
def greet_user():
    """��ʾ�򵥵��ʺ���"""
    print("Hello!")
    
greet_user()
print("\n")

# part_1.1 ����������Ϣ
def greet_user(username):
    """��ʾ�򵥵��ʺ���"""
    print("Hello, " + username.title() + "!")
    
greet_user('ten')
print("\n")

# part_1.2 ʵ�κ��β�
def lover(name,age):
    """��ʾ���˵������Լ�����"""
    print(name + ", ���� "+ str(age) +"��.")
    
lover('�Ƴ���',21)

# ������ʾ name age ���β�  '�Ƴ���',21��ʵ��

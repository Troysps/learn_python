# coding=gbk
# �ھ��� ��
# part_9.1 �������ʹ����

# part_9.1.1 ������
# ʹ��class��� �Լ���д����ĸ������
class Dog():
    """һ��ģ��С���ļ򵥳���"""
    
    def __init__(self,name,age):
        # �����еĺ�����Ϊ���� ����һ������ķ��� ��ͷ�ͽ�β���������»�����������ͨ����
        """��ʼ������name��age"""
        self.name = name
        self.age = age
        # ��selfΪǰ׺�ı��������������е����з���
        # ��Ҫ�������ֺ�����ʱ ����self�� �Զ�����
        # �������ֺ�������Щ������ʱ�� ͨ��self.name = name ��ȡ�洢���β��е�ֵ
        # ��Ϊͨ��ʵ������    ʵ�����ʵı�����Ϊ����
        
    def sit(self):
        """ģ��С�����������"""
        print(self.name.title(),"is now sitting.")
        # ���巽��  ����ģ��ʵ�����
        
    def roll_over(self):
        """ģ��С��������ʱ���"""
        print(self.name.title()," rolled over!")
        


# part_9.1.2 �����ഴ��ʵ��
my_dog = Dog('jen',8)

print("My dog's name is",my_dog.name.title(),".")
print("My dog is",str(my_dog.age),"years old.")


# part_9.1.2.1 �������� ʹ�þ���ʾ�� ��ʽ: my_dog.name


# part_9.1.2.2 ���÷���
my_dog.sit()
my_dog.roll_over()

print("\n")
# part_9.1.2.3 �������ʵ��   ���԰���ʵ�ʵ����󴴽�����������ʵ��
l_dog = Dog('hong',3)
c_dog = Dog('cai',2)

print("Lei dog's name is",l_dog.name.title(),".")
print("Lei dog is",str(l_dog.age),"years old.")
l_dog.sit()
print("\n")
print("Cai dog's name is",c_dog.name.title(),".")
print("Cai dog is",str(c_dog.age),"years old")
c_dog.roll_over()


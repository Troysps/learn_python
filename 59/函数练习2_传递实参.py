# coding=gbk
# ������ϰ_2 ����ʵ��

# part_2.1 λ��ʵ�� ÿ��ʵ�ζ������Ӧ���β�
def describe_pets(animal_type,pet_name):
    """��ʾ��������������"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pets('dog','sam')
# ˳�����ʾ�� �βκ�ʵ�ε�˳��һһ��Ӧ
describe_pets('sam','dog')
# ���������Ե��﷨����

# ͨ����������ʾ���Է��� λ��ʵ�ε��������Ե��ص�
# part_2.1.1 ���Ե��ú������
# part_2.1.2 λ��ʵ�ε�˳������Ҫ

# part_2.2 �ؼ���ʵ�� ��ʵ�ν��и�ֵ ����˳����޹ؽ�Ҫ
describe_pets(pet_name='sam',animal_type='dog')
# ֵ�� ��ʵ���н��βκ�ֵ�������� ����Ҫ����˳��

# Part_2.3 Ĭ��ֵ ��ÿ���β�ָ��Ĭ��ֵ
def describe_pets(pet_name,animal_type='dog'):
    """��ʾ��������������"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pets(pet_name='jen')

# ���������޸����βε�λ�� ��򵥵�д��Ӧ������:
describe_pets('ten')

# part_2.4 ��Ч�ĺ������� ���ݺ��������ַ���:λ��ʵ�� �ؼ���ʵ�� Ĭ��ֵ ���Ի���

# part_2.5 ����ʵ�δ��� �����﷨�����ʱ��ؿ� Traceback 


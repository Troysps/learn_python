# coding=gbk
# ����part_3 ����ֵ ����return���

# part_3.1 ���ؼ�ֵ
def get_formatted_name(first_name, last_name):
    """�������������"""
    full_name = first_name + " " + last_name
    return full_name.title()
    
musician = get_formatted_name('jen', 'hex')
print(musician)

# return��䷵�ص��ú����Ĵ�����
# ���÷���ֵ�ĺ�����Ҫ���ϱ���

# part_3.2 ��ʵ�α�ɿ�ѡ ����λ��ʵ�� ʹ��Ĭ��ֵ������ʵ�α�ɿ�ѡ
def get_formatted_name(first_name, middle_name, last_name):
    """�������������"""
    full_name = first_name + " " +middle_name + " " + last_name
    return full_name.title()
    
musician = get_formatted_name('jen' , 'lei', 'fu')
print(musician)

# ���������м�û�� ��ô���Ե����βε�λ�� �Լ�Ĭ��ֵ
def get_formatted_name(first_name, last_name, middle_name = ''):
    """�������������"""
    if middle_name:
        full_name = first_name + " " +middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
    
musician = get_formatted_name('lei', 'fu')
print(musician)

musician = get_formatted_name('lei', 'fu' ,'tian')
print(musician)

# if��� λ��ʵ�� Ĭ��ֵ

# part_3.3 �����ֵ� �������п������� �ֵ� �б� �ַ��� ��ֵ ��һ��������ʾ
def build_person(first_name, last_name):
    """����һ���ֵ䣬 ���а����й�һ���˵���Ϣ"""
    person = {'first' : first_name, 'last' : last_name}
    return person
    
musician = build_person('jen', 'hex')
print(musician)

#  �����ֵ� �洢����
def build_person(first_name, last_name, age = ''):
    """����һ���ֵ� ���а����й�һ���˵���Ϣ"""
    person = {
    'first' : first_name,
    'last' : last_name,
    }
    if age:
        person['age'] = age
    return person
    
musician = build_person('jen', 'ten', age=27)
print(musician)

# part_3.4 ���ʹ�ú�����whileѭ�� 
def get_formatted_name(first_name, last_name):
    """�������������"""
    full_name = first_name + " " + last_name
    return full_name.title()
    
# ����ѭ��
while True:
    print("\nPlease tell me your name : ")
    print("Enter 'q' at any time quit.")
    f_name = input("First name : ")
    
    if f_name == 'q':
        break

    l_name = input("Last name : ")
    if l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    

    

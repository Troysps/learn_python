# coding=gbk

# ���������б�_part4
# �������Դ��������С���б�
def greet_user(names):
    """���б��е�ÿλ�û������ʺ�"""
    for name in names:
        msg = "Hello," + name.title() + "!"
        print(msg)
usernames = ['ten','lei','tianfu']
greet_user(usernames)
print("\n")
# part_4.1 ���ú������б�֮��Ĵ�������

# whileѭ�������б�֮���Ԫ��
# ���ȴ��������б� һ�����б� һ���ǿ��б�
unprinted_designs = ['iphone cases','robot pendant','dodacahedron']
completed_models = []

# ģ���ӡÿ����ƣ�֪��û��Ϊֹ
# ����ӡ�õ���ƣ��ƶ����б�completed_models
while unprinted_designs:
    current_design = unprinted_designs.pop()
    
    # ģ������������3D��ӡģ�͵Ĺ���
    print("Printing model:",current_design)
    completed_models.append(current_design)
    
# ��ʾ��ӡ�õ�����ģ��
print("\nThe following models have been printed:")
print(completed_models)

print("\n")
# ����ʹ�ú����� ��ʹ���б������޵��޸Ŀ���
# ������������ ��һ���������ʾ ģ���ӡÿ����� �������ƶ����Ѵ�ӡ���б�
# �ڶ����������ʾ ��ʾ��ӡ�õ�����ģ��

# ��һ������
def print_models(unprinted_designs,completed_models):
    """
    ģ���ӡÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ
    ��ӡÿ����ƺ󣬶������ƶ����б�completed_models��
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # ģ��������������3D��ӡģ�͹���
        print("Printing model:",current_design)
        completed_models.append(current_design)
        
# �ڶ�������
def show_printed_models(completed_models):
    """��ʾ�Ѵ�ӡ������ģ��"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    
unprinted_designs = ['lei','tian','fu']
completed_models = []

print_models(unprinted_designs,completed_models)
show_printed_models(completed_models)


print("\n")
# part4.2 ��ֹ�����޸��б� ������Ƭ��ʾ�������б�ĸ���

# �����ݷ������� ԭʼ������Ϊ��Ҫ ����Ҫ�μ���Ƭ��ʾ��
unprinted_designs = ['huang','cheng','hong']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_printed_models(completed_models)

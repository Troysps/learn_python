# coding=utf-8
# ��whileѭ�������б���ֵ�

# part_1 ���б�֮���ƶ�Ԫ��
# ���ȴ���һ��δ��֤�û����б�
# �ٴ���һ���洢�Ѿ���֤�û��Ŀ��б�
uncomfirmed_users = ['jen','ten','lei']
comfirmed_users = []
# ��֤ÿ���û�ֱ��û��Ϊֹ
# ��ÿ����֤���û��洢������֤�û���
while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()
    
    print("Verifying user : " + current_user.title())
    comfirmed_users.append(current_user)
    
# ��ʾ�����Ѿ���֤���û�
print("\nThe following users have been comfirmed : ")
for comfirmed_user in comfirmed_users:
    print(comfirmed_user.title())
print("\n")
# ���÷���pop()��δ��֤�б�����ȡ����ɾ��Ԫ��
# ��չ�����Լ�������֤���û����д���Ԫ�� ��ʾ�û�������֮�� �����û����ѱ�ע��
# ���ǲ�Ӱ���������û����� �������֤���û�����

# part_2 ɾ�������ض�ֵ�������б�Ԫ��
pets = ['cat','cat','cat','dog','goldfish','rabbit']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
print("\n")
# �ͺ���set()��ȫ��ͬ ���Ƿ���remove()

# part_3 ʹ���û�����������ֵ�
responses = {}

# ����һ����־��ָ�������Ƿ����
polling_active = True

while polling_active:
    # ��ʾ���뱻�����ߵ����ֺͻش�
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # ���ش������������ֵ�
    responses[name] = response
    # ����ѭ��ֹͣ��·��
    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False
# �����������ʾ���
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name+" would you like to climb " + response + ".")
            

# ���Գ��������û�ѡ���Ƿ����ش�

# ��һ��������Ϸ

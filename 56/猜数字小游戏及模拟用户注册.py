# coding=gbk
# �û������whileѭ���Է���ϰ
# 1.������С��Ϸ
# 2.�û�������ƶ��б�Ԫ������-ģ���û�ע��


# 1.������С��Ϸ
print("������������һ��������С��Ϸ�ɣ���ֵ��0��100֮��.")
number = 66

while True:
    guess_number = input("������µ���ֵ��! ")
    message = int(guess_number)
    
    if message > 66:
        print("��ʾ:��ֵû��ô��")
        
    elif (message < 66) and (message > 60):
        print("��ʾ:����һ��.")
        
    elif (message <= 60) and (message >= 0):
        print("��ʾ:��ֵû��ôС")
        
    elif message == 66:
        print("��ʾ:��ϲ��¶���")
        break
print("\n")
# 2.ģ���û�ע��
new_user = []
confirmed_users = ['��ٻ','�����','�̼Ҷ�','����','������']

while True:
    prompt = "����������û���: "
    username = input(prompt)
    new_user.append(username)    
    
    if username in confirmed_users:
        print("�����û����ѱ�ע��")

    elif username not in confirmed_users:
        confirmed_users.append(username)
        print("����ע��ɹ�����ͨ����֤")
        
    message = input("�Ƿ����ע��: ")
    if message == '��':
        break
# ��ʾ��ͨ����֤�������û��Լ���������ȫ���û�
print(new_user)

print(confirmed_users)


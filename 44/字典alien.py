# coding=gbk
# �ֵ�

# һ�����ֵ�
alien_0 = {'color':'green','point':5}

print(alien_0['color'])
print(alien_0['point'])
print("\n")
# �����ֵ��е�ֵ ָ���ֵ��� ���ڷ����ŵļ�
alien_0 = {'color':'green','point':5}
new_alien = alien_0['color']
print("You just killed "+new_alien+" alien.")
# ����ʹ���˱��������ֵ��е�ֵ
print("\n")

# ��Ӽ�_ֵ�� ����ָ���ֵ��� �÷���������ļ����������ֵ
alien_0 = {'color':'green','point':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n")

# �ȴ���һ�����ֵ�
alien_0 = {}

alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)
print("\n")
# �޸��ֵ��е�ֵ
alien_0 = {"color":"green"}
print(alien_0)
alien_0['color'] = "yellow"
print(alien_0)
print("\n")
# ɾ����_ֵ��
alien_0 = {'color':'green','point':5}
del alien_0['color']
print(alien_0)
print("\n")
# �����ƶ�����ɵ��ֵ�
favorite_languages = {
    'jen':'java',
    'yunten':'java',
    'tianfu':'python',
    'phil':'c',
    }
    
print("Tianfu's favorite language is "+favorite_languages['tianfu'].title()+".")
print("\n")
# Ȥζ��ϰ �޸������˵��ٶ� �Ӷ��ƶ�λ��
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position :"+str(alien_0['x_position']))

# �����ƶ�������
# ���������˵��ٶ��ƶ�����
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # ����������ٶ�һ���ܿ�
    x_increment = 3
    
# ��λ�õ�����λ�ü�������
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("Now x-position : "+str(alien_0['x_position']))

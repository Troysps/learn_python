# coding=gbk
# part_1 ���ֵ���ϰ1�е�һϵ��print����滻Ϊ�����ֵ��еļ���ֵ��ѭ��
sikan_information = {'frist_name':'chen',
    'slast_name':'sikan',
    'age':21,
    'city':'guangzhou'
        }

for sikan,information in sorted(sikan_information.items()):
    print(sikan+" : "+str(information))

print("\n")
cute_number = {'python':1,
    'java':2,
    'c':3,
    'html':4,
    'php':5
    }

for language in sorted(cute_number.keys()):
    print(language)
    
print("\n")
��̴ʻ� = {'�ַ���':'�����֡���ĸ���»�����ɵ�һ���ַ�',
    '�б�':'��һϵ���ض�˳�����е�Ԫ�����',
    'Ԫ��':'�����޸ĵ��б�',
    '�ֵ�':'һϵ�м�_ֵ��',
    '��̻����ṹ':'��䡢�������������ؼ���',
        }
        
for n,meaning in ��̴ʻ�.items():
    print(n+" : "+meaning+".")
print("\n")

��̴ʻ�['����'] = '�ú���set()��ʾ��һ���б��ж�һ�޶���Ԫ����ȡ����������һ�б�'
��̴ʻ�['����sorted()'] = '���б�Ԫ�ذ���ĸ˳���������'
��̴ʻ�['forѭ��'] = '�����б��е�ÿ��Ԫ�� ����ִ����ͬ�Ĳ���'
��̴ʻ�['if���'] = '������������ ֻ��һ�����Ժ�һ������'
��̴ʻ�['�������ʽ'] = '������������'
print(��̴ʻ�)
print("\n")
for n,m in ��̴ʻ�.items():
    print(n+" : "+m)

print("\n")
# part_2 �����ֵ��еļ�ֵ�� �� ֵ
river_country = {'changjiang' : 'china',
    'huanghe' : 'chian',
    'nile' : 'egypt',
    }
    
for river,country in river_country.items():
    print("The "+river.title()+" runs through "+country.title()+".")
    print(river.title())
    print(country.title())

print("\n")    
# part_3 �����ֵ���if���
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
    
people = ['jen','phil']
for man in favorite_languages.keys():
    if man in people:
        print(man.title()+" , Thank you for your help!")
    else:
        print("Help me! "+man.title())

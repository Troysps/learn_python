# coding=gbk
# �����ֵ�

# part1 �������еļ�-ֵ�� ����items() ע�ⷵ��˳��ʹ���˳���ǲ�һ����
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# part2 �����ֵ����еļ� ����keys() 
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for name in sorted(favorite_languages.keys()):
    print("\n"+name)
print("\n")    
# part3 �����ֵ����е�ֵ ����values() ��ȡ�б��е�����Ԫ�� �������ظ�
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
    
for language in favorite_languages.values():
    print(language)

print("\n")
# ʹ�ú���set() ���б����ҳ���һ�޶���Ԫ�� �������� 
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for language in set(favorite_languages.values()):
    print(language)    
    
print("\n")
# ���Ժ���set() �Ƿ���ֵ�ļ�����һ�� �ҳ���һ�޶��ļ�  ����ͨ������һ�� 
favorite_languages = {
    'jen':'python',
    'jen':'c',
    'edward':'ruby',
    'phil':'python',
    }
for people in set(favorite_languages.keys()):
    print(people)

print("\n")
# ���Ժ���set() �����ֵ�ļ�ֵ����ô�� ��Ч�� ����ÿ�η���˳��������� �ʹ洢˳���޹�
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for people,language in set(favorite_languages.items()):
    print(people+" : "+language) 

print("\n")
# ���Ժ���set() �����б�   ˳�����к���sorted()����
alberts = ['a','b','c','a']
for n in sorted(set(alberts)):
    print(n)
    
print("\n")
# ��˳������ֵ����Եļ�_ֵ�� ����sorted()  ͬ���������м� ֵ  ���з���reverse()
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }

for key,value in sorted(user_0.items()):
    print(key+" : "+value)

# �������� Ҫע��set() ����Ӧ�����ֵ�ļ���ֵ�� �Լ��б���
# ����˳��Ŀǰ�Ǻ���sorted() ����sort() �Լ� ����reverse()������
print("\n")
# С��ϰ �ֵ���б����
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

friends = ['jen','sarah']
for name in favorite_languages:
    print(name.title()+" favorite language is "+favorite_languages[name]+".")
    
    if name in friends:
        print(name.title())

print("\n")

# ���Ըı�ṹ ��ͬ����֮ǰ�Ŀ���ָ�������б�Ķ��󵥶�����ָ��������߲��� ǰ����ȫ�� �����ǲ��ཻ���Ӽ�
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

friends = ['jen','sarah']
for name in favorite_languages:
    if name in friends:
        print(name.title())
    else:
        print(name.title()+" favorite language is "+favorite_languages[name]+".")


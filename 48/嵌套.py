# coding=gbk
# Ƕ�� ��һϵ���ֵ�洢���б��� ���б���Ϊֵ�洢���ֵ���
# �б��д洢�ֵ� �ֵ��д洢�б� �ֵ��д洢�ֵ�
# part_1 �б��д洢�ֵ�
alien_0 = {'color' : 'green','points' : 5}
alien_1 = {'color' : 'yellow','points' : 10}
alien_2 = {'color' : 'red','point' : 15}

aliens = [alien_0,alien_1,alien_2]
print(str(aliens)+"\n")

for alien in aliens:
    print(str(alien))
print("\n")
# Сϸ��������ֵ�ʱ�� ���ú���str()

# С��ϰ������һ�����������˵��б� 30����ɫ�� 5�� ����������
aliens = []
for alien in range(0,30):
    new_alien = {'color' : 'green',
        'point' : 5,
        'speed' : 'slow',
        }
    aliens.append(new_alien)
print(str(aliens)+"\n")
# �������б��ҳ���
# ������ʾǰ�������������
for alien in aliens[0:5]:
    print(alien)
print("...")
# ��ʾ�����˶���������
print("Total number of aliens : "+str(len(aliens)))
print("\n")

# С��ϰ����δ����Ⱥ��ӵ�������  
for alien in range(0,30):
    new_alien = {'color' : 'green',
        'point' : 5,
        'speed' : 'slow',
        }
    aliens.append(new_alien)
# ����Ӧ��forѭ��if��佫�б��ǰ����������������
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
# ��ʾǰ���������
for alien in aliens[:5]:
    print(alien)
print("...")
print("\n")
# ʹ�õ���forѭ�� if��� �����б� ������Ƭ ����range() str() ����append()
# ������ʹ��if_elif�����
# С��ϰ�����޸�
for alien in range(0,30):
    new_alien = {'color' : 'green',
        'point' : 5,
        'speed' : 'slow',
        }
    aliens.append(new_alien)
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = '15'
        alien['speed'] = 'fast'
for alien in aliens[:10]:
    print(alien)

print("\n")

# ����Ҫ��������������Ľ������ִ��һ��֮��Ͳ�ִ����if����ص�

# part_2���ֵ��д洢�б� Ҳ�����ֵ��еļ���Ӧ���ֵʱʹ��
pizza = {'crust' : 'thick',
    'topping' : ['mushroom','extra cheese']
    }
# ���������pizza
print("You ordered a "+pizza['crust']+"-crust pizza "
    +"with the following toppings:")
for topping in pizza['topping']:
    print(topping)
# С��ϰ����Щ��ϲ����������
favorite_language = {
    'ten' : ['java','c'],
    'troy' : ['python','java'],
    'phil' : ['ruby','php'],
    'edward'   : ['ruby'],
    }

for name,language in favorite_language.items():
    print("\n"+name.title()+"'s favorite languages are :")
    for language in language:
        print("\t"+language.title())

# Part_3 ���ֵ��д洢�ֵ� ����ֵ��
user = {
    'aeinstein': {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for n,m in user.items():
    print("\nusername :"+n)
    full_name = m['first']+m['last']
    location = m['location']
    
    print("\tFull name : "+full_name.title())
    print("\tLocation : "+location.title())


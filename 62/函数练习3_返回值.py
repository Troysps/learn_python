# coding=gbk
# ������ϰ3 ����ֵ

# part_1 �򵥷���ֵ��ϰ
def city_country(city, country):
    """���к͹���"""
    belong = city + ", " + country
    return belong.title()
    
konw = city_country('shanghai','china')
print(konw)

konw = city_country('shenzheng','china')
print(konw)

konw = city_country('newyork','american')
print(konw)

print("\n")

# part_2 �����д����ֵ䲢����
def make_album(person, album):
    """����ר�����ֵ� ����ר�� ��ֵ��"""
    alum = {'person' : person.title(), 'album' : album.title()}
    return alum
    
make = make_album('justin', 'love')
print(make)

make = make_album('nile', 'fucl')
print(make)

make = make_album('lei', 'woca')
print(make)

# ��ӿ�ѡ����
def make_album(person, album,number = ''):
    """����ר�����ֵ� ����ר�� ��ֵ��"""
    album = {
    'person' : person.title(), 
    'album' : album.title(),
    }
    
    if number:
        album['number'] = number
    return album
make = make_album('you' ,'like')
print(make)

make = make_album('i' ,'hate', number=10)
print(make)

# ������ֵΪ0ʱ���Զ�����

# part_3 ���whileѭ�����û����� д���� ����ֵ
def make_album(person, album, number = ''):
    """����ר�����ֵ� ����ר�� ��ֵ��"""
    album = {
    'person' : person.title(), 
    'album' : album.title(),
    'number' : number
    }
    return album
    
while True:
    print("\nPlease enter these information: ")
    print("Enter 'q' at any time to quit.")
    p_seron = input("person: ")
    a_lbum = input("album: ")
    n_umber = input("number: ")
        
    if p_seron == 'q':
        break
        
    if a_lbum == 'q':
        break
    
    if n_umber == 'q':
        break
        
    make = make_album(p_seron, a_lbum, n_umber)
    print(make)

# ע���ʽ!!!

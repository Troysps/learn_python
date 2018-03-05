# coding=gbk
# 函数练习3 返回值

# part_1 简单返回值练习
def city_country(city, country):
    """城市和国家"""
    belong = city + ", " + country
    return belong.title()
    
konw = city_country('shanghai','china')
print(konw)

konw = city_country('shenzheng','china')
print(konw)

konw = city_country('newyork','american')
print(konw)

print("\n")

# part_2 函数中创建字典并返回
def make_album(person, album):
    """创建专辑的字典 人与专辑 键值对"""
    alum = {'person' : person.title(), 'album' : album.title()}
    return alum
    
make = make_album('justin', 'love')
print(make)

make = make_album('nile', 'fucl')
print(make)

make = make_album('lei', 'woca')
print(make)

# 添加可选参数
def make_album(person, album,number = ''):
    """创建专辑的字典 人与专辑 键值对"""
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

# 发现数值为0时会自动忽略

# part_3 结合while循环和用户输入 写函数 返回值
def make_album(person, album, number = ''):
    """创建专辑的字典 人与专辑 键值对"""
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

# 注意格式!!!

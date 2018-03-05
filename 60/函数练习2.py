# coding=gbk
# 函数练习2 

# part_1 使用位置实参调用 关键字实参调用
def make_shirt(size,words):
    """制作衣服的尺码与字样"""
    print("\nThe T-shirt size is " + size.title() +" and a word in here : "+ words)
    
make_shirt('m','I love u')

make_shirt(words='I love u',size='m')

# part_2 使用默认值
def make_shirt(size,words='I love Python'):
    """制作衣服的尺码与字样"""
    print("\nThe T-shirt size is " + size.upper() +" and a word in here : "+ words)
    
make_shirt('m')

make_shirt(size='xxxl')

# part_3 等效的函数调用
def describe_city(city,country='china'):
    """城市及从属的国家"""
    print("\n" + city.title() + " belongs to " +country.title() + '.')
    
describe_city('shanghai')
describe_city('beijing')
describe_city('newyork',country='amerian')



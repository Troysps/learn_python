# coding=gbk
# ������ϰ2 

# part_1 ʹ��λ��ʵ�ε��� �ؼ���ʵ�ε���
def make_shirt(size,words):
    """�����·��ĳ���������"""
    print("\nThe T-shirt size is " + size.title() +" and a word in here : "+ words)
    
make_shirt('m','I love u')

make_shirt(words='I love u',size='m')

# part_2 ʹ��Ĭ��ֵ
def make_shirt(size,words='I love Python'):
    """�����·��ĳ���������"""
    print("\nThe T-shirt size is " + size.upper() +" and a word in here : "+ words)
    
make_shirt('m')

make_shirt(size='xxxl')

# part_3 ��Ч�ĺ�������
def describe_city(city,country='china'):
    """���м������Ĺ���"""
    print("\n" + city.title() + " belongs to " +country.title() + '.')
    
describe_city('shanghai')
describe_city('beijing')
describe_city('newyork',country='amerian')



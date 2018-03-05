# coding=gbk
# ������ϰ5 ������ ���������ʵ�� 

# part_1 ���������ʵ�� ���β�ǰ�ӵ��Ǻ� ��������Ϊ�β����Ŀ�Ԫ��
def sandwich_toppings(size,*toppings):
    """��ʾ�����εĴ�С������"""
    print("\nMake a",str(size),"inch sandwish .")
    print("The following toppings is:")
    for topping in toppings:
        print("\t",topping)
        
sandwich_toppings(18,'fruit')
sandwich_toppings(20,'apple','banana','beff')

# part_2 ���������ֵ� ʹ�ú��� ���ֵ��������Լ�
def build_profile(first,last,**user_info):
    """����һ���ֵ䣬���а�������֪�����й��û���һ��"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k,v in user_info.items():
        profile[k] = v
    return profile
    
my_profile = build_profile(
    'lei',
    'tianfu',
    location = 'shengzhen',
    lover = 'huangchenghong'
    )
    
print(my_profile)

# part_3 ��д���� �����ֵ� ���β�֮ǰʹ��˫�Ǻ�** ������Ϊ�β����Ŀ��ֵ�
def make_car(brand,model,**other):
    """��ʾ������Ʒ�� �ͺ� ����������Ϣ"""
    like_car = {}
    like_car['brand'] = brand
    like_car['model'] = model
    for k,v in other.items():
        like_car[k] = v
    return like_car
    
car = make_car(
    'bmw',
    'm',
    color = 'black',
    tow_package = True
    )
    
print(car) 

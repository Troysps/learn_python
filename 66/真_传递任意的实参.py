# coding=gbk
# ���������ʵ��

# part_5.1 �β���ǰ��1���Ǻ� * ������Ϊ�βεĿ�Ԫ��
def make_pizza(*topping):
    """��ӡ�˿͵����������"""
    print(topping)
    
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
# ��ס��ӡ���������Ԫ��
print("\n")
# С��ϰ
def make_pizza(*toppings):
    """����Ҫ�����ı���"""
    print("\nMaking a pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


# ���ʹ��λ��ʵ�κ���������ʵ��   �β���ʵ��һһ��Ӧ
def make_pizza(size,*toppings):
    """����Ҫ����������"""
    print("\nMaking a",str(size),"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-",topping)
        
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


# ʹ�����������Ĺؼ���ʵ��
# -�β���ǰ��˫�Ǻ� ������Ϊ�βεĿ��ֵ�
# ˫�Ǻ��β� �������������Ĺؼ���ʵ��

def build_profile(first,last,**user_info):
    """����һ���ֵ䣬���а�������֪�����й��û���һ��"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k,v in user_info.items():
        profile[k] = v
    return profile
    
user_profile = build_profile('albert','einstein',
    location='princeton',
    field='physics')
    
print(user_profile)

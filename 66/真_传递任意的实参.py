# coding=gbk
# 传递任意的实参

# part_5.1 形参面前加1个星号 * 创建名为形参的空元组
def make_pizza(*topping):
    """打印顾客点的所有配料"""
    print(topping)
    
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
# 记住打印出来最后是元组
print("\n")
# 小练习
def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


# 结合使用位置实参和任意数量实参   形参与实参一一对应
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMaking a",str(size),"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-",topping)
        
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


# 使用任意数量的关键字实参
# -形参名前加双星号 创建名为形参的空字典
# 双星号形参 接收任意数量的关键字实参

def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
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

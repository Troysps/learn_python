# coding=gbk
# 函数练习5 函数体 传递任意的实参 

# part_1 传递任意的实参 在形参前加单星号 创建了名为形参名的空元组
def sandwich_toppings(size,*toppings):
    """显示三明治的大小，配料"""
    print("\nMake a",str(size),"inch sandwish .")
    print("The following toppings is:")
    for topping in toppings:
        print("\t",topping)
        
sandwich_toppings(18,'fruit')
sandwich_toppings(20,'apple','banana','beff')

# part_2 函数创建字典 使用函数 在字典中描述自己
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
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

# part_3 编写函数 创建字典 在形参之前使用双星号** 创建名为形参名的空字典
def make_car(brand,model,**other):
    """显示汽车的品牌 型号 及其他的信息"""
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

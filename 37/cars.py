# coding=gbk
# if_else语句处理列表特殊元素
# 检查是否相等 ==
cars=['bwm','audi','subaru','toyota']
for car in cars:
    if car == 'bwm':  
        print(car.upper())
    else:
        print(car.title())
        
        
# 检查是否不等 !=
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

even_numbers=list(range(1,100000001,2))
print(even_numbers)

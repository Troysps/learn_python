# coding=gbk
# if语句处理列表
# part_1 处理列表特殊元素 for循环之后接if语句
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping.title()+".")
print("\nFinished making your pizza!")
print("\n")
# part_2 确定列表是不是空的 if语句后接for循环
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plan pizza?")
print("\n")
# part_3 使用多个列表
avaliable_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print("Adding"+requested_topping.title()+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
print("\nFinished making your pizza.")


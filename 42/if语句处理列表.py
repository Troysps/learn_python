# coding=gbk
# if��䴦���б�
# part_1 �����б�����Ԫ�� forѭ��֮���if���
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping.title()+".")
print("\nFinished making your pizza!")
print("\n")
# part_2 ȷ���б��ǲ��ǿյ� if�����forѭ��
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plan pizza?")
print("\n")
# part_3 ʹ�ö���б�
avaliable_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print("Adding"+requested_topping.title()+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
print("\nFinished making your pizza.")


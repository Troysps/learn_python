# coding=gbk
# ������ϰ6 �������洢��ģ���� 
# ʹ��import ���

def make_pizza(size,*toppings):
    """����Ҫ����������"""
    print("\nMake a",str(size),"inch pizza with the following toppings:")
    for topping in toppings:
        print("-",topping)

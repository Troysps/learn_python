# coding=utf-8
# �û������whileѭ����ϰ

# part_1 �б�֮��ת��Ԫ��
sandwich_orders = ['fruit sandwish','tuna sandwish','beef sandwish']
finished_sandwiches = []
# ѭ��sandwich_orders������ȡ���е�Ԫ��
while sandwich_orders:
    order = sandwich_orders.pop()
    print("\tsandwiches : "+ order.title())
    
    finished_sandwiches.append(order)
# ��ʾ��������֤��sandwiches
print("\nThe following sandwich have been comfirmed:")
for finished in finished_sandwiches:
    print(finished)
print("\n")
# part_2 ɾ���б��е��ض�ֵ
sandwich_orders = ['fruit sandwish','tuna sandwish','beef sandwish']
for order in range(3):
    # ����ֻ�ǵ����ĸ����������ѭ�����ٴΣ�ÿִ��һ�ξʹ���һ��pastrami sandwich
    new_order = 'pastrami sandwich'
    sandwich_orders.append(new_order)
    
print(sandwich_orders)

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

print("\n"+str(sandwich_orders))

# part_3 ʹ���û������whileѭ�������ֵ�
users_responses = {}

# ���ñ�־
active = True

while active:
    # ��ʾ�û�����
    name = input("Hei!Plz enter your name: ")
    place = input("One place in the world , where would you go? ")
    # ���û���������ֵ�
    users_responses[name] = place

    repeat = input("Enter 'quit':quit the responses. ")
    if repeat == 'quit':
        active = False
# ��ʾ������
for name,place in users_responses.items():
    print(name+" : "+place)

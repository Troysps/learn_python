# coding=gbk
# part_1 ��whileѭ��
topping = "Hei Sir,What topping do you want? "

while True:
    message = input(topping)
    if message == "quit":
        break
    else:
        print("The "+message+" will add in pizza.")
# ���ñ�־�Լ�break���
        
# part_2 ʹ��continue���
message = "Please enter your age: "

while True:
    visitor_age = input(message)
    if visitor_age == "quit":
        break
    visitor_age = int(visitor_age)
    if visitor_age < 3:
        price = 0
    elif (visitor_age) >= 3 and (visitor_age <= 12):
        price = 10
    elif visitor_age > 12:
        price = 15


    print("The sale price is "+str(price)+".")
    
# ʹ��������if����������

# ��������ֻ��if����forѭ�����в���


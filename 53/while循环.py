# coding=gbk
# part_1 简单while循环
topping = "Hei Sir,What topping do you want? "

while True:
    message = input(topping)
    if message == "quit":
        break
    else:
        print("The "+message+" will add in pizza.")
# 活用标志以及break语句
        
# part_2 使用continue语句
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
    
# 使用了两个if语句灵活运用

# 可以试试只用if语句个for循环看行不行


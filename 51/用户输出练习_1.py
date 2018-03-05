# coding=gbk
# part_1 租赁汽车 使用函数input()
car = input("Hello,Sir!Which car do you need? ")
print("Let me see if I can find you a "+car+".")

# part_2 用户输入加上if语句 int()
seat = input("Hello,Sir!How mang people of you come here for dinner? ")
seat = int(seat)
if seat >= 8:
    print("Sorry.Here is no empty table")
else:
    print("OK,we have an empty table.Waiting for you.")

# part_3 运算符(%)
number = "Please enter an number.I will tell you if it's "
number += "the integer times of ten? "
number = input(number)
number = int(number)

if number % 2 == 0:
    print("\n"+str(number)+" is the integer times of ten.")
else :
    print("\n"+str(number)+" is not the integer times of ten.")


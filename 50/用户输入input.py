# coding=gbk
# �û����룡��������
message = input("Tell me something,and I will repeat it back to you: ")
print(message)

# ��д�����ĳ���
name = input("Please enter you name: ")
print("Hello, "+name+" !")

# ʹ�������+= 
prompt = "If you tell us who are you, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello ,"+name+"!")

# ����int()
height = input("How tall are you? ")
height = int(height)

if height >= 1.8:
    print("You are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# ��ģ�����(%)
number = input("Enter a number,and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number "+ str(number) +" is even.")
else:
    print("\nThe number "+ str(number) +" is odd.")
    

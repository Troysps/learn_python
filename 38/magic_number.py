# coding=gbk
# �Ƚ�����"
# ����> ���ڵ���>= С��< С�ڵ���<=
answer = 17
if answer != 42:
      print("That is not the correct answer.Please try again!")

import this

# ��������� and or 
answer = 19
if (answer > 10) and (answer < 20):
    print("You are right!")

if (answer >= 19) or (answer <5):
    print("Right!")

# ����ض�ֵ�Ƿ�������б��� �ؼ��� in
requested_topping=['mushrooms','onions','pineapple']
if "mushrooms" in requested_topping:
    print("OK!")

# ����ض�ֵ�Ƿ񲻰������б��� �ؼ��� not in
banned_user = ['andrew','carolina','david']
user = 'marie'
if user not in banned_user:
    print(user.title()+ ", you can post a response if you wish.")

jacks=[]
for a in range(2,50000000,2):
    jacks.append(a)
for b in range(50000002,100000000,2):
    jacks.append(b)
print(jacks)    


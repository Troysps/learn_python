my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print(my_foods)
print(friend_foods)
#coding=gbk
#切片练习
print("The first three items in the list are:")
print(my_foods[0:3])

print("The middle three items in the list are:")
print(my_foods[1:4])

print("The last three items in the list are:")
print(my_foods[-3:])

my_foods.append('cannoli')
friend_foods.append('ice cream')
for i in my_foods:
    print(i)
print(my_foods)
for friend in friend_foods:
    print(friend)
print(friend_foods)


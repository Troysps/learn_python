
#循环练习
magicans=['alice','david','carolina']
for magican in magicans:
    print(magican.title()+",that was a great trick!")
    print("I can't wait to see your next trick, "+magican.title()+".\n")
    
print("Thank you,everyone.That was a great magic show!")

pizzas=['durian','fruit','beef']
for pizza in pizzas:
    print(pizza)
    print("I like "+pizza+"!"+"\n")

print("I really like pizza.")

pets=['cat','dog','tiger','lion']
for pet in pets:
    print("A "+pet+" would make a great pet.")
print("\n"+"Any of these animals would make a great pet!")

#复制列表
friend_pizzas=pizzas[:]
pizzas.append('apple')
friend_pizzas.append('banana')
print("My favorite pizzas are:")
for i_like in pizzas:
    print(i_like)
print("My friend favorite pizzas are:")
for friend_like in friend_pizzas:
    print(friend_like)

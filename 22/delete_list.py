#coding=gbk
#三种删除 del语句 pop()方法 remove()方法
motorcycles=['honda','yahama','sukuzi']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles.append('yahama')
print(motorcycles)

motorcycles[1]='sukuzi'
print(motorcycles)

motorcycles.insert(0,'honda')
print(motorcycles)

poped_motorcycles=motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

vehicles=['car','trian','airplane','bicycle']
poped_vehicles=vehicles.pop(0)
print(vehicles)

vehicles.remove('bicycle')
print(vehicles)

too_expensive='airplane'
vehicles.remove(too_expensive)
print(vehicles)
print("\nA "+too_expensive.title()+" is too expensive for me.")


# coding=gbk
# for 循环
for number in range(1,21):
    print(number)


# for 循环步长
for square in range(1,21,2):
    print(square)

parts=[]
for part in range (3,31,3):
    parts.append(part/3)
print(parts)
# for 循环 创建列表
skys=[]
for sky in range(1,11):
    skys.append(sky**3)
print(skys)
for sky in skys:
        print(sky)
# 列表解析
loves=[love**3 for love in range(1,11)]
print(loves)
# 最小值 最大值 和 函数
jacks=list(range(1,1000001))
print(jacks)
print(min(jacks))
print(max(jacks))
print(sum(jacks))

# 元组
dimensions=('c','s')
print(dimensions[0])
print(dimensions[1])


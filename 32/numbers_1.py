# coding=gbk
# for ѭ��
for number in range(1,21):
    print(number)


# for ѭ������
for square in range(1,21,2):
    print(square)

parts=[]
for part in range (3,31,3):
    parts.append(part/3)
print(parts)
# for ѭ�� �����б�
skys=[]
for sky in range(1,11):
    skys.append(sky**3)
print(skys)
for sky in skys:
        print(sky)
# �б����
loves=[love**3 for love in range(1,11)]
print(loves)
# ��Сֵ ���ֵ �� ����
jacks=list(range(1,1000001))
print(jacks)
print(min(jacks))
print(max(jacks))
print(sum(jacks))

# Ԫ��
dimensions=('c','s')
print(dimensions[0])
print(dimensions[1])


# coding=gbk
# ����ѧϰ6 �������洢��ģ����

# part_6.1 ��������ģ��
# ��ʽ��import��� ������
import pizza

pizza.make_pizza(18,'apple')
pizza.make_pizza(233,'apple','banana','beef')

# part_6.2 �����ض��ĺ��� ģ�����ض��ĺ���
# ��ʽ��from �ļ��� import ������

from pizza import make_pizza

pizza.make_pizza(100,'fuck you')

# part_6.3 ʹ��as������ָ������
# from �ļ��� import ������ as ָ������

from pizza import make_pizza as fuck

fuck(999,'��ʺ��')
fuck(1000,'����������','����')

# part_6.4 ʹ��as��ģ��ָ������

import pizza as p

p.make_pizza(233333,'��ƨ��')
p.make_pizza(199999,'��ǰ��ѧ����ѧ','mdzz')

# part_6.5 ����ģ���е����к���
# ʹ���Ǻ�* �ɵ���ģ���е����к���

from pizza import *

make_pizza(100000,'��')
make_pizza(200000,'��')



# coding=gbk
# ������ϰ6 �������洢��ģ���� 
# Ӧ�ú���
import show_printed_model


def print_models(unprinted_designs,completed_models):
    """
    ģ���ӡÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ
    ��ӡÿ����ƺ󣬶������ƶ����б�completed_models��
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # ģ��������������3D��ӡģ�͹���
        print("Printing model:",current_design)
        completed_models.append(current_design)


n = ['s','d','e']
m = []
print_models(n,m)
show_printed_model.show_printed_models(m)

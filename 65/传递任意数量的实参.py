# coding=gbk
# �����ħ��ʦ 
# �ؼ���enumerate������


names = ['liuqian','zhoujielun','jay']
new_names =[]

def make_great(magicians_name):
    """�޸�ħ��ʦ�б�"""
    for index,magician in enumerate(magicians_name):
        magicians_name[index] = 'the Great ' + magician
        new_names.append(magicians_name[index])
        
def show_magicians(magicians_name):
    """��ӡħ��ʦ������"""
    for magician in magicians_name:
        print(magician)
        
make_great(names[:])

show_magicians(new_names)
show_magicians(names)




# coding=gbk
# 不变的魔术师 
# 关键字enumerate！！！


names = ['liuqian','zhoujielun','jay']
new_names =[]

def make_great(magicians_name):
    """修改魔术师列表"""
    for index,magician in enumerate(magicians_name):
        magicians_name[index] = 'the Great ' + magician
        new_names.append(magicians_name[index])
        
def show_magicians(magicians_name):
    """打印魔术师的名字"""
    for magician in magicians_name:
        print(magician)
        
make_great(names[:])

show_magicians(new_names)
show_magicians(names)




# coding=gbk
# ������ϰ4

# part_1 �������������С���б�
def show_magicians(magicians):
    """��ÿλ������ݵ�ħ��ʦ�ʺ�"""
    for magician in magicians:
        print("Hello,",magician,"!")
    



# part_2 �����޸��б�  ������������

def make_great(magicians):
    """��ħ��ʦǰ�����the Great"""
    for index,magician in enumerate(magicians):
        magicians[index] = 'the Great ' + magician
        

def main():
    magicians = ['lei','huang','jen']
    
    if not magicians:
        print("magicians is None")
        return
        
    print("magician:")
    show_magicians(magicians)
    print("----")
    print("the Great magician:")
    make_great(magicians)
    show_magicians(magicians)
    
if __name__ =="__main__":
    main()

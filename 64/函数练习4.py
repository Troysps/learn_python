# coding=gbk
# 函数练习4

# part_1 函数处理任意大小的列表
def show_magicians(magicians):
    """向每位参与表演的魔术师问好"""
    for magician in magicians:
        print("Hello,",magician,"!")
    



# part_2 函数修改列表  创建俩个函数

def make_great(magicians):
    """在魔术师前面加上the Great"""
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

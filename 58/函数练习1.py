# coding=gbk
# ������ϰ

# part_1 ��д����������
def display_message(topic):
    """�ڰ���ѧϰ����"""
    print("Chapter 8 learning " + topic.title() + ".")

display_message('functions')
print("\n")

# part_2 ��д���������β� Ӧ��ʵ��
def favorite_book(title):
    """��ϲ�����鱾"""
    print("One of my favorite book is "+title.title())

favorite_book('alice in wonderland')
favorite_book('learning python')

# ����ֻ��һ���βε�ʱ���Ƿ���Զ�Ӧ���޵�ʵ��
favorite_book('python','nnnnn')
# �βκ�ʵ��һһ��Ӧ!



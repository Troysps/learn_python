# coding=gbk
# 9.4 ���������ϰ

"""�йز�������"""

class Restaurant():
    """����һ����������"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """��ʼ���������ֺ���⿷�ʽ"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """���е�һ������ ��������"""
        print("\n" + self.restaurant_name.title(),"located in Shenzhen.")
        print("Cuisine Type :",self.cuisine_type)
        
    def open_restaurant(self):
        """���е�һ������ ָ����������Ӫҵ"""
        print(self.restaurant_name.title(),"now is opening")
        

        

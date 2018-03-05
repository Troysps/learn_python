# coding=gbk
# 9.4 导入类的练习

"""有关餐厅的类"""

class Restaurant():
    """创建一个餐厅的类"""
    
    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐厅名字和烹饪方式"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """类中的一个方法 描述餐厅"""
        print("\n" + self.restaurant_name.title(),"located in Shenzhen.")
        print("Cuisine Type :",self.cuisine_type)
        
    def open_restaurant(self):
        """类中的一个方法 指出餐厅正在营业"""
        print(self.restaurant_name.title(),"now is opening")
        

        

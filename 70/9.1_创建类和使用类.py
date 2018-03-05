# coding=gbk
# 第九章 类
# part_9.1 创建类和使用类

# part_9.1.1 创建类
# 使用class语句 以及大写首字母定义类
class Dog():
    """一次模拟小狗的简单尝试"""
    
    def __init__(self,name,age):
        # 在类中的函数称为方法 这是一个特殊的方法 开头和结尾各有两个下划线以区别普通方法
        """初始化属性name和age"""
        self.name = name
        self.age = age
        # 以self为前缀的变量可以用在类中的所有方法
        # 需要传递名字和年龄时 都在self中 自动传递
        # 访问名字和年龄这些变量的时候 通过self.name = name 获取存储在形参中的值
        # 称为通过实例访问    实例访问的变量称为属性
        
    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title(),"is now sitting.")
        # 定义方法  用来模拟实际情况
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()," rolled over!")
        


# part_9.1.2 根据类创建实例
my_dog = Dog('jen',8)

print("My dog's name is",my_dog.name.title(),".")
print("My dog is",str(my_dog.age),"years old.")


# part_9.1.2.1 访问属性 使用句点表示法 格式: my_dog.name


# part_9.1.2.2 调用方法
my_dog.sit()
my_dog.roll_over()

print("\n")
# part_9.1.2.3 创建多个实例   可以按照实际的需求创建任意数量的实例
l_dog = Dog('hong',3)
c_dog = Dog('cai',2)

print("Lei dog's name is",l_dog.name.title(),".")
print("Lei dog is",str(l_dog.age),"years old.")
l_dog.sit()
print("\n")
print("Cai dog's name is",c_dog.name.title(),".")
print("Cai dog is",str(c_dog.age),"years old")
c_dog.roll_over()


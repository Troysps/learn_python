# -*- coding:utf-8 -*-
# 11.2测试类

# 11.2.1 掌握各种各样的断言方法
# assertEqual(a, b) 核实a == b
# asserNotEqual(a, b) 核实 a != b
# assertTrue(x) 核实x为True
# assertFalse(y) 核实y为False
# assertIn(item, list) 核实item在list里面
# assertNotIn(item, list) 核实item不在list里面

# 11.2.2 一个要测试的类
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    
    def __init__(self, question):
        """存储问题,并为储存答案做准备"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """方法 显示问题"""
        print(self.question)
        
    def stored_response(self, new_response):
        """方法 存储单个问题"""
        self.responses.append(new_response)
        
    def show_results(self):
        """方法 显示收集到的所有答案"""
        print("Survey results:")
        for response in self.reponses:
            print("-",response)
            

# -*- coding:utf-8 -*-

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
        for response in self.responses:
            print("-",response)
            

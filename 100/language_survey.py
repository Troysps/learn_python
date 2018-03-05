# -*- coding:utf-8 -*-
# 11.2.2 测试类的基本思路

from survey import AnonymousSurvey

# 定义一个问题,并创建一个表示调查的AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' to quit at any time.")
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.stored_response(response)
    
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

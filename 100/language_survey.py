# -*- coding:utf-8 -*-
# 11.2.2 ������Ļ���˼·

from survey import AnonymousSurvey

# ����һ������,������һ����ʾ�����AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# ��ʾ���Ⲣ�洢��
my_survey.show_question()
print("Enter 'q' to quit at any time.")
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.stored_response(response)
    
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

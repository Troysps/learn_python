# -*- coding:utf-8 -*-
# 11.2.3 导入unittest模块测试类


# 每一个方法都创建了一个AnonymousSurvey类的实例 并在这些方法中创建了答案
# 使用方法setUp()创建一个调查对象以及一组答案以供测试的方法使用
if __name__ == '__main__':
    import unittest
    from survey import AnonymousSurvey

    class TestAnonymousSurvey(unittest.TestCase):
        """测试AnonymousSurvey类"""
    
        def setUp(self):
            """创建一个调查对象和一组答案,以供测试的方法使用"""
            question = "What language did you first learn to speak?"
            self.my_survey = AnonymousSurvey(question)
            self.responses = ['English', 'Chinese', 'Mandarin']
        
        def test_store_single_response(self):
            """测试单个答案被存储"""
            self.my_survey.stored_response(self.responses[0])
            self.assertIn(self.responses[0], self.my_survey.responses)
        
        def test_three_responses_store(self):
            """测试三个答案被存储"""
            for response in self.responses:
                self.my_survey.stored_response(response)
            for response in self.responses:
                self.assertIn(response, self.my_survey.responses)


    unittest.main()

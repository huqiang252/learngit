# -*- coding: utf-8 -*-
class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.成绩 = int(input('请输入考试成绩：'))

    @classmethod
    def 计算是否及格(cls):
        if cls.成绩 >= 60:
            return '及格'
        else:
            return '不及格'

    @classmethod
    def 考试结果(cls):
        result=cls.计算是否及格()
        if result=='及格':
            print(cls.学生姓名+'同学考试通过了啦！')
        elif result=='不及格':
            print(cls.学生姓名+'需要补考')


成绩单.录入成绩单()
成绩单.考试结果()
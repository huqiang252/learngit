# -*- coding: utf-8 -*-
class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 =int(input('请输入数学成绩：'))
    @classmethod
    def 打印成绩单(cls):
        print(cls.学生姓名 + '的成绩单如下：')
        print('语文成绩：' + str(cls.语文_成绩))
        print('数学成绩：' + str(cls.数学_成绩))

    @classmethod
    def 打印平均分(cls):
        cls.平均成绩=float((cls.语文_成绩+cls.数学_成绩)/2)
        return cls.平均成绩

    @classmethod
    def 评级(cls):
        #调用类的其他方法
        cls.打印平均分()
        print('两科的平均成绩：' + str(cls.平均成绩))
        if cls.平均成绩>=90:
            print('优')
        elif cls.平均成绩>=80:
            print('良好')
        elif cls.平均成绩>=70:
            print('一般')
        else:
            print('差')


成绩单.录入成绩单()
成绩单.打印成绩单()
成绩单.评级()
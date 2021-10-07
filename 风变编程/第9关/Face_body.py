# -*- coding: utf-8 -*-

# def face(name):
#     return name+'的脸蛋'
#
# def body(name):
#     return  name+'的身材'
#
# def main(dream_face,dream_body):
#     return '我的梦中情人：'+face(dream_face)+'和'+body(dream_body)
#
# print(main('刘亦菲','林志玲'))
# print(main('李若彤','王珞丹'))

def lover(face_name,body_name):
    return face_name+'的脸蛋',body_name+'的身材'

girl=lover('李若彤','侯佩岑')
print(girl)
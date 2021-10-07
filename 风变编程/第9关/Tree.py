# -*- coding: utf-8 -*-
#圣诞老人树
def tree(Height):

    print('Merry Christmas!')

    for i in range(Height):

        print((Height-i)*2*' '+'o'+ i*'~x~o')

        print(((Height-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')


tree(10)

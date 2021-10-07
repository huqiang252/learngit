# -*- coding: utf-8 -*-
import math
def yuan(R):
    S=math.pi*(R**2)
    L=2*(math.pi)*R
    return S,L

def show(R):
    top=yuan(R)
    print('半径为'+str(R)+'的面积：'+str(top[0]))
    print('半径为'+str(R)+'的周长：'+str(top[1]))

show(3)
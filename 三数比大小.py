# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:12:26 2021

@author: 常自昂
"""

def f(a,b,c):
    min=max=a
    if(b>max):
        max=b
    if(c>max):
        max=c
    if(b<min):
        min=b
    if(c<min):
        min=c
    return max, min
x,y,z=eval(input("请输入3个值："))
max,min=f(x,y,z)
print("max=",max,"min=",min)

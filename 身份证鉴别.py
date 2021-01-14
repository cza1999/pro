# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:12:30 2021

@author: 常自昂
"""
def verifyCardID():
    #验证前17位
    factor=( 7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
    #最后一位身份证号
    last=("1", "0", "X","9","8","7","6","5","4","3","2")
    while True:
        strCardID=input( "Please Input ID card num ( 'q’for Exit):")
        if strCardID=='q':
            break
        if len(strCardID)!=18:
            print("Please enter again2: ")
        else:
            sum1=0
            for i in range(17):
                sum1+=int(strCardID[i])*factor[i]
            if last[sum1%11]==strCardID[17]:
                if int(strCardID[16])% 2==0:
                    print("ID card num is legal女性!")
                else:
                    print("ID card num is legal男性!")
            else:
                print( "ID card num is illegal \n!")
verifyCardID()

    


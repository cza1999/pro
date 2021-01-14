# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:48:20 2021

@author: 常自昂
"""
#读读读读读读读读读读读读读读读读读读读读读读读读读读读读读
#以二进制形式打开文件
with open( '数据库demo.txt' ,"rb") as f:
    print(f.readline())#读取一行

#以文本文件方式打开,默认
f=open( '数据库demo.txt' ,"rt",encoding=("utf-8"))
#print(f.readlines())#读取所有行，生成列表
#print(f.read())#文件内容原样输出
#for i in f.readlines():#逐行
for i in f.read():#每行一字
    print(i)#逐行
#print(f.readlines())#读取一行
f.close()


# =============================================================================
# r 只读 w 覆盖写 无则创建存则覆盖 x 创建写 无则创建存则报错 a 追加写 无则创建存则追加 b 二进制 t 文本文件 
# + 与r/w/x/a使用
# =============================================================================
#写写写写写写写写写写写写写写写写写写写写写写写写写写写写

fname=input("要写入内容的文件名字：")
fo=open(fname,"a+",encoding=("utf-8"))
ls=["\n","1212\n","123123\n","12341234\n"]
fo.writelines(ls)#写入一个元素全为字符串的列表
#fo.write("aaaaa")
fo.seek(1)#0-文件开头 1-当前位置 2 文件结尾
for line in fo:
    print(line)
fo.close()

#在文件开头插入内容不能用“a+”
fname=input("要写入内容的文件名字：")
fo=open(fname,"r+",encoding=("utf-8"))
#fo.seek(0)
fo.write("55555\n")
fo.seek(0)
print(fo.read())
#fo.seek(0)#0-文件开头 1-当前位置 2 文件结尾
fo.close()

#开头插入内容，会覆盖原有文件内容
fo=open("1.txt","r+",encoding=("utf-8"))
fo.seek(2)
fo.write("1\n2\n9")
fo.seek(0)
print(fo.read())
#fo.seek(0)#0-文件开头 1-当前位置 2 文件结尾
fo.close()

f=open("练习.txt","x+",encoding=("utf-8"))
f.write("ddd测试\nfsvsvsv\ndfhbdgnbtd\nsdfvgsfvgs")
f.close()

f=open('数据库demo.txt' ,"a+")
f.write( '\ndddgfgh ')
f.close() 

with open("jieba.txt","w+",encoding=("utf-8")) as f:
    d=["做梦 3","理想 4"]
    f.writelines(d)
    print(f.read())


























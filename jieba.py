# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:24:00 2021

@author: 常自昂
"""

import jieba
import jieba.posseg as pseg
#精确模式：把文本精确的切分开，不存在冗余单词
#全模式：把文本中所有可能的词语都扫描出来，有冗余
#搜索引擎模式：在精确模式基础上，对长词再次切分
ss = "你是想红寺湖但行好事时尚先生"
jieba.add_word("理想")
print(jieba.lcut_for_search(ss))#搜索引擎模式：在精确模式的基础上，对长词再次进行切分
print(jieba.lcut(ss,cut_all=True))#全模式：将语句中所有可能是词的词语都切分出来，速度很快，但是存在冗余数据
print(jieba.lcut(ss))#精确模式，返回一个 列表类型，建议使用
pseg.lcut(ss) #词性
f=jieba.load_userdict("jieba.txt")#为自定义词典的路径
# =============================================================================
# 词典格式一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开
# =============================================================================
import jieba
def getText():
    txt=open("jieba.txt","r+",encoding=("utf-8")).read()
    txt=txt.lower()
    for ch in "!@#$%^&*()":
        txt=txt.replace(ch," ")
    return txt
h=getText()
#words=h.split()
words=jieba.lcut(h)
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(30):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word, count))






































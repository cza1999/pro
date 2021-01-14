# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 09:42:18 2020

@author: 常自昂
"""
import jieba
excludes = {}
#excludes = {"1801120077","如何","牛肉汤"}
txt = open("数据库demo.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 0:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(40):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))

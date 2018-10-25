#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 创建一些实验样本
# 1. 进行词条切分后的文档集合
# 2. 类别标签的集合,
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'],
            ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
            ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
            ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
            ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
            ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1] # 1 代表侮辱性文字 0 代表正常言论
    return postingList, classVec

# 创建一个包含在所有文档中出现的词集合列表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# 输入为词汇表, 某个文档
# 输出为文档向量,向量的每个元素为1或0,分别表示词汇表中的单词在输入文档中是否出现.
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print ("the word: %s is not in my Vocabulary!" % word)
    
    return returnVec



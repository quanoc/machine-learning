#!/usr/bin/python
# -*- coding: UTF-8 -*-

import bayes

listOposts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOposts)

print (myVocabList)

res = bayes.setOfWords2Vec(myVocabList, listOposts[0])
print (res)

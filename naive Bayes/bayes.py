# -*- coding: utf-8 -*-
"""
bayes
~~~~~
copy from *machine learning in action*

abbreviation
~~~~~~~~~~~~
- Vec   = Vector
- Vocab = Vocabulary
"""


def loadDataSet():
    postingList = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid'],
    ]
    # 1 is abusive, 0 not
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        # Why use "|", See http://blog.csdn.net/business122/article/details/7541486
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWord2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print('the word: %s is not in my Vocabulary!' % word)
    return returnVec

if __name__ == '__main__':
    listOposts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOposts)
    print(myVocabList)
    print(setOfWord2Vec(myVocabList, listOposts[0]))
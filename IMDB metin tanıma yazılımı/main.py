# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:43:12 2022

@author: kundakci
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from bs4 import BeautifulSoup
import re
import nltk
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords

# veri setimizi yüklüyoruz
df = pd.read_csv('NLPlabeledData.tsv', delimiter='\t', quoting=3)

nltk.download('stopwords')


# VERİ TEMİZLEME İŞLEM
sample_review = df.review[0]


# ilk olarak html taglerinin temizlenmesi
sample_review = BeautifulSoup(sample_review).get_text()

# noktalma işaretleri ve sayılardan temizleme sayılar duygu analizinde işe yaramıyor...
sample_review = re.sub("[^a-zA-Z]", ' ', sample_review)

# küçük harflere dönüştürme işlemi yapıyoruz çünkü büyük harfle başlayan kelimeleri farklı bir kelime olarak algılıyor...
sample_review = sample_review.lower()


# stopwords yani the, is are gibi kelimeler yapay zeka tarafından kullanılmasın istiyoruz bunlar grammer kelimeler...
# önce split ile kelimeleri bölüyoruz ve listeye dönüştüyoruz. amacımız stopwords kelimleri çıkarmak...
sample_review = sample_review.split()

swords = set(stopwords.words('english'))
sample_review = [w for w in sample_review if w not in swords]


# temizleme işleminin mantığını anladığımıza göre şimdi tüm dataframe için bu işlemi yapabiliriz....
def process(review):
    # review html
    review = BeautifulSoup(review).get_text()
    # review punctuation and numbers
    review = re.sub("[^a-zA-Z]", ' ', review)
    # converting into lowercase and spliting to eliminate stopwords
    review = review.lower()
    review = review.split()
    swords = set(stopwords.words('english'))
    review = [w for w in review if w not in swords]
    # ayrılmış kelimelerin birlşetirilmesi
    return(" ".join(review))


train_x_tum = []
for r in range(len(df["review"])):
    if(r+1) % 100 == 0:
        print("no of reviews processed =", r+1)
    train_x_tum.append(process(df["review"][r]))


# TRAIN TEST SPLIT....
x = train_x_tum
y = np.array(df["sentiment"])

# train test split
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1)


# bag of words oluşturuyoruz
# yapay zeka kelimlerden anlamaz bizde bu kelimeleri sayılardan oluşan bir matrix e çeviriyoruz...
vectorizer = CountVectorizer(max_features=5000)

# train veri setimizi feature vektör matrixine çeviriyoruz
train_x = vectorizer.fit_transform(train_x)

# ranomforest modeli oluşutuyoruz...
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(train_x, train_y)

# şimdi testdatamızda
test_xx = vectorizer.transform(test_x)
test_xx = test_xx.toarray()



test_predict = model.predict(test_xx)
dogruluk = roc_auc_score(test_y, test_predict)
print("Doğruluk oranı : % ", dogruluk * 100)

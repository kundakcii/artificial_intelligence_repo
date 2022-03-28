# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:47:54 2022

@author: kundakci
"""

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("DecisionTreesClassificationDataSet.csv")
# IseAlindi columns kategorik verisini numeric hale çevirilmesi..
duzeltme_IseAlindi = pd.get_dummies(df['IseAlindi'])
duzeltme_IseAlindi = duzeltme_IseAlindi.iloc[:, 1:]
duzeltme_IseAlindi.rename(columns={'Y': 'IseAlindi'}, inplace=True)


# SuanCalisiyor columns kategorik verisinin numereic hale çevirilmesi...
duzeltme_SuanCalisiyor = pd.get_dummies(df['SuanCalisiyor?'])
duzeltme_SuanCalisiyor = duzeltme_SuanCalisiyor.iloc[:, 1:]
duzeltme_SuanCalisiyor.rename(columns={'Y': 'SuanCalisiyor?'}, inplace=True)

# Top10 Universite? columns kategorik verisinin numereic hale çevirilmesi...
duzeltme_TopU = pd.get_dummies(df['Top10 Universite?'])
duzeltme_TopU = duzeltme_TopU.iloc[:, 1:]
duzeltme_TopU.rename(columns={'Y': 'Top10 Universite?'}, inplace=True)

# StajBizdeYaptimi? columns kategorik verisinin numereic hale çevirilmesi...
duzeltme_staj = pd.get_dummies(df['StajBizdeYaptimi?'])
duzeltme_staj = duzeltme_staj.iloc[:, 1:]
duzeltme_staj.rename(columns={'Y': 'StajBizdeYaptimi?'}, inplace=True)

# Egitim Seviyesi columns kategorik verisinin numereic hale çevirilmesi...
# LabelEncoder kullanarak her bir kategoriye bir sayı atamsı yapılır.
duzeltme_egitim = LabelEncoder().fit_transform(df['Egitim Seviyesi'])
duzeltme_egitim = pd.DataFrame(duzeltme_egitim, columns=['Egitim Seviyesi'])

y = duzeltme_IseAlindi
x = pd.concat([df['Deneyim Yili'], duzeltme_SuanCalisiyor,
               df['Eski Calistigi Firmalar'], duzeltme_egitim, duzeltme_TopU, duzeltme_staj, ], axis=1)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

print (clf.predict([[5, 1, 3, 0, 0, 0]]))
print (clf.predict([[2, 0, 7, 0, 1, 0]]))
print (clf.predict([[2, 1, 7, 0, 0, 0]]))
print (clf.predict([[20, 0, 5, 1, 1, 1]]))


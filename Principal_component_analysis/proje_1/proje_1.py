# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:03:38 2022

@author: kundakci
"""

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

url = "pca_iris.data"

df = pd.read_csv(url, names=[
    "sepal length", "sepal width", "petal length", "petal width", "target"])


# featurlerı  x olarak ayıralım
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df[features]

# target'i y olarak ayıralım
y = df[['target']]


# değerlerin scale edilmesi
x = StandardScaler().fit_transform(x)


# PCA PROJECTİON 4 BOYUTTAN 2 BOYUTA İNDRİME

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)

principalDF = pd.DataFrame(data=principalComponents, columns=[
                           'principal components 1', 'principal components 2'])
final_dataframe = pd.concat([principalDF, df[['target']]], axis=1)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['g', 'b', 'r']

plt.xlabel('principal components 1')
plt.ylabel('principal components 2')

for target, col in zip(targets, colors):
    dftemp = final_dataframe[df.target == target]
    plt.scatter(dftemp['principal components 1'],
                dftemp['principal components 2'], color=col)

#varyans kaybı sorgulama
explained_variance = pca.explained_variance_ratio_
evrs = pca.explained_variance_ratio_.sum()

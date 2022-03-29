# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:04:11 2022

@author: kundakci
"""

import pandas as pd
import sklearn.metrics as metrics
import sklearn.cluster as cluster
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv('Avm_Musterileri.csv')


plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'])
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()
# yeniden isimlendirme
df.rename(columns={'Annual Income (k$)': 'income'}, inplace=True)
df.rename(columns={'Spending Score (1-100)': 'score'}, inplace=True)


# Normalization
scaler = MinMaxScaler()

scaler.fit(df[['income']])
df['income'] = scaler.transform(df[['income']])

scaler.fit(df[['score']])
df['score'] = scaler.transform(df[['score']])

# Silhouette Method
for i in range(2, 13):
    label = cluster.KMeans(n_clusters=i, init='k-means++',
                           random_state=20).fit(df).labels_
    print("Silhouette Method score for k(clusters)= " + str(i) + " is " + str(metrics.silhouette_score(df, label,
                                                                                                       metric="euclidean", sample_size=1000, random_state=20)))

kmeans = cluster.KMeans(n_clusters=5, init='k-means++')
kmeans = kmeans.fit(df[['score', 'income']])


df['Clusters']=kmeans.labels_
sns.scatterplot(x='score',y='income',hue='Clusters',data=df)
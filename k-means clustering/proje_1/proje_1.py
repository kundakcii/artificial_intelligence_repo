# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:46:36 2022

@author: kundakci
"""

from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

df = pd.read_csv('Avm_Musterileri.csv')


plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'])
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

# Ture dersek direk dataframe de değiştirir false derse yeni bir data frame oluşturur ve yeni bir değişkene atama yapmalısın...
df.rename(columns={'Annual Income (k$)': 'income'}, inplace=True)
df.rename(columns={'Spending Score (1-100)': 'score'}, inplace=True)


# Normalizetaion
scaler = MinMaxScaler()

scaler.fit(df[['income']])
df['income'] = scaler.transform(df[['income']])

scaler.fit(df[['score']])
df['score'] = scaler.transform(df[['score']])

# İLK OLARAK K DEĞERİNİ BELİRLEYELİM
k_range = range(1, 20)

list_dist = []

for i in k_range:
    kmeans_model = KMeans(n_clusters=i)
    kmeans_model.fit(df[['income', 'score']])
    list_dist.append(kmeans_model.inertia_)

plt.xlabel('K')
plt.ylabel('Distortion değeri (inertia)')
plt.plot(k_range, list_dist)
plt.show()

# burada bulunan en iyi k değeri
kmeans_model = KMeans(n_clusters=5)
y_predicted = kmeans_model.fit_predict(df[['income', 'score']])
df['cluster'] = y_predicted

df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]
df4 = df[df.cluster == 3]
df5 = df[df.cluster == 4]


plt.xlabel('income')
plt.ylabel('score')
plt.scatter(df1['income'], df1['score'], color='green')
plt.scatter(df2['income'], df2['score'], color='red')
plt.scatter(df3['income'], df3['score'], color='black')
plt.scatter(df4['income'], df4['score'], color='orange')
plt.scatter(df5['income'], df5['score'], color='purple')


plt.scatter(kmeans_model.cluster_centers_[:, 0], kmeans_model.cluster_centers_[
            :, 1], color='blue', marker='X', label='centroid')
plt.legend()
print(plt.show())

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:54:54 2022

@author: kundakci
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from kmodes.kprototypes import KPrototypes
from kmodes.kmodes import KModes


df = pd.read_csv('segmentation_data.csv')

# 'ID', 'Age', 'Income'  bir kenara aldım
df_temp = df[['ID', 'Age', 'Income']]

# boş verilerin toplamını görmek için...
null_data = df.isnull().sum()


scaler = MinMaxScaler()
scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])

# ID column ın silinmesi
df = df.drop(['ID'], axis=1)

# kullandığımız model float ile çalıştığı için datasetimizdeki int değerleri float a çeviriyoruz...
mark_array = df.values
mark_array[:, 2] = mark_array[:, 2].astype(float)
mark_array[:, 4] = mark_array[:, 4].astype(float)


# modelin kurulması
kproto = KPrototypes(n_clusters=10, verbose=2, max_iter=20)
clusters = kproto.fit_predict(mark_array, categorical=[0, 1, 3, 5, 6])
print(kproto.cluster_centroids_)
len_cluster = len(kproto.cluster_centroids_)

cluster_dict = []
for c in clusters:
    cluster_dict.append(c)

df['cluster'] = cluster_dict

df[['ID', 'Age', 'Income']] = df_temp

cluser_0_ten = df[df['cluster'] == 0].head(10)

# yaşa ve gelire göre nasıl bir ayrım yapmış bunun görselleştirilmesi

df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]
df4 = df[df.cluster == 3]
df5 = df[df.cluster == 4]
df6 = df[df.cluster == 5]
df7 = df[df.cluster == 6]
df8 = df[df.cluster == 7]
df9 = df[df.cluster == 8]
df10 = df[df.cluster == 9]
df11 = df[df.cluster == 10]

plt.figure(figsize=(15, 15))
plt.xlabel('Age')
plt.ylabel('Income')

plt.scatter(df1.Age, df1['Income'], color='green', alpha=0.4)
plt.scatter(df2.Age, df2['Income'], color='red', alpha=0.4)
plt.scatter(df3.Age, df3['Income'], color='gray', alpha=0.4)
plt.scatter(df4.Age, df4['Income'], color='orange', alpha=0.4)
plt.scatter(df5.Age, df5['Income'], color='yellow', alpha=0.4)
plt.scatter(df6.Age, df6['Income'], color='cyan', alpha=0.4)
plt.scatter(df7.Age, df7['Income'], color='magenta', alpha=0.4)
plt.scatter(df8.Age, df8['Income'], color='gray', alpha=0.4)
plt.scatter(df9.Age, df9['Income'], color='purple', alpha=0.4)
plt.scatter(df10.Age, df10['Income'], color='blue', alpha=0.4)
plt.scatter(df11.Age, df11['Income'], color='pink', alpha=0.4)

plt.legend()
plt.show()


plt.figure(figsize=(15, 15))
plt.xlabel('Education')
plt.ylabel('Income')
print()

plt.scatter(df1.Education, df1['Income'], color='green', alpha=0.4)
plt.scatter(df2.Education, df2['Income'], color='red', alpha=0.4)
plt.scatter(df3.Education, df3['Income'], color='gray', alpha=0.4)
plt.scatter(df4.Education, df4['Income'], color='orange', alpha=0.4)
plt.scatter(df5.Education, df5['Income'], color='yellow', alpha=0.4)
plt.scatter(df6.Education, df6['Income'], color='cyan', alpha=0.4)
plt.scatter(df7.Education, df7['Income'], color='magenta', alpha=0.4)
plt.scatter(df8.Education, df8['Income'], color='gray', alpha=0.4)
plt.scatter(df9.Education, df9['Income'], color='purple', alpha=0.4)
plt.scatter(df10.Education, df10['Income'], color='blue', alpha=0.4)
plt.scatter(df11.Education, df11['Income'], color='pink', alpha=0.4)

plt.legend()
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 16:35:45 2022

@author: kundakci
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Outcome = 1  Diabet/Şeker hastası
# Outcome = 0 Sağlıklı

data = pd.read_csv('diabetes.csv')
data.head()
seker_hastalari = data[data.Outcome == 1]
saglikli_insanlar = data[data.Outcome == 0]

# şimdilik sadece gloucose 'a bakarak örnek bir çizim yapalım:
# programımızın sonunda makine öğrenmesi modelimiz sadece glikoza değil, tüm diğer verilere bakarak bir tahmin yapacaktır.
plt.scatter(saglikli_insanlar.Age, saglikli_insanlar.Glucose,
            color='green', label='Sağlıklı', alpha=0.4)
plt.scatter(seker_hastalari.Age, seker_hastalari.Glucose,
            color="red", label="Diabet hastası", alpha=0.4)
plt.xlabel("Age")
plt.ylabel("Glucose")
plt.legend()
plt.show()

# x ve ye eksenlerini belirleyelim
# kişi hastamı hasta değilmi ayıralım
y = data.Outcome.values
x_ham_veri = data.drop(["Outcome"], axis=1)
# Outcome sütununun(dependet variable) çıkarıp sadece independet variables bırakıyoruz.
# çünkü KNN algoritması x değerleri içerisinde gruplandırma yapacak.

# Normalization yapıyoruz - x_ham_veri içerisindeki değerleri sadece 0 ve 1 arasında olacak şekilde hepsini güncelliyoruz.
# eğer bu şekilde normalization yapmazsak yüksek rakamlar küçük rakamları ezer ve KNN algoritmasını yanıltabilir.
x = (x_ham_veri - np.min(x_ham_veri))/(np.max(x_ham_veri)-np.min(x_ham_veri))


# Train datamız ile test datamızı ayırıyoruz.
# Train datamız sistemin sağlıklı insan ile hasta insanı ayırt etmesini öğrenmek için kullanılacak
# Test datamız ise modelimiz test etmek için kullanılacak
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)


# KNN modelimizi oluşturuyoruz...

knn = KNeighborsClassifier(n_neighbors=3)  # n_neighbors = k
knn.fit(x_train, y_train)
prediction = knn.predict(x_test)
print("K=3 için Test verilerimizin doğrulama testi sonucu: ",
      knn.score(x_test, y_test))

# K Kaç olmalı ???
# En iyi K değerini belirleyelim.
sayac = 1
for k in range(1, 11):
    knn_yeni = KNeighborsClassifier(n_neighbors=k)
    knn_yeni.fit(x_train, y_train)
    print(sayac, " ", "Doğruluk oranı: %", knn_yeni.score(x_test, y_test)*100)
    sayac += 1

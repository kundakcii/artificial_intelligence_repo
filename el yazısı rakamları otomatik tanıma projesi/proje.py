# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:59:32 2022

@author: kundakci
"""

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

mnist = fetch_openml('mnist_784')

datashape = mnist.data.shape

# mnist veriseti içindeki rakam fotoğraflarını görmek için bir fonksiyon tanımlayalım...


def showimages(dframe, index):
    some_digit = dframe.to_numpy()[index]
    some_digit_image = some_digit.reshape(28, 28)

    plt.imshow(some_digit_image, cmap='binary')
    plt.axis('off')
    print(plt.show())


showimages(mnist.data, 1)

# test ve train oranı 1/7 ve 6/7
train_img, test_img, train_lbl, test_lbl = train_test_split(
    mnist.data, mnist.target, test_size=1/7.0, random_state=0)
print(type(train_img))
# rakam tahminlerini check etmek için train_img dataframe 'in bir kopyasını alıyoruz çünkü az sonra değişecek....
test_img_copy = test_img.copy()
showimages(test_img_copy, index=0)

# VERİLERİMİZİ SCALE ETMEMİZ GEREKİYOR:
# çünkü PCA scale edilmemiş verilerde hatalı sonuç verebiliyor bu nedenle mutlaka scaling işleminden geçiyoru.Bu amaçla StandarScaler kullanıyoruz...

scaler = StandardScaler()

# scaler'ı sadece training set üzerinde fit yapmamız yeterli
scaler.fit(train_img)

# Ama transform işlemini hem training sete hemde test sete yapmamız gerekiyor...
train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)

# PCA işlemini uyguluyoruz.
# Variance 'nin %95 oranında korunmasını istediğimizi belirtiyoruz.

# Make an instance of the model
pca = PCA(.95)

# PCA' i sadece training sete yapmamız yeterli
pca.fit(train_img)

# bakalım 784 boyutu kaç boyuta düşürebilmiş (%95 varience koruyarak)
print(pca.n_components_)

# şimdi transform işlemiyle hem train hemde test veri setimizin boyutlarını 784 ' ten 327 ' ye düşürelim...
train_img = pca.transform(train_img)
test_img = pca.transform(test_img)

# default solver çok yavaş çalıtığı için daha hızlı olan 'lbfgs' solver ' ı seçerek logisticregression nenemizi oluşturuyoruz.
logisticRegr = LogisticRegression(solver='lbfgs', max_iter=10000)


# LogisticRegression modelimizi train datamızı kullanarak eğitiyoruz...
logisticRegr.fit(train_img, train_lbl)


# model eğitildi şimdi el yazısı rakamları makine öğrenmesi ile tanıma işlemini gerçekleştrelim

print(logisticRegr.predict(test_img[0].reshape(1, -1)))
showimages(test_img_copy, 0)
print(logisticRegr.predict(test_img[2].reshape(1, -1)))
showimages(test_img_copy, 2)


# Modelimizin doğruluk oranı (accuracy) ölçmek için score metodunu kullanacağız:

logisticRegr.score(test_img, test_lbl) 

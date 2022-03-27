# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:14:57 2022

@author: kundakci
"""
# Multiple linear regression 'da birdan fazla bağımsız(independent) değişkene karşılık bir bağımlı(depenndt) değişken vardır.
# Linear Regression veriler arasında var olan korelasyonu(ilişkiyi) kullanarak yeni gelecek verileri tahmin etme modelidir.
# burda makine öğrenimi bize veriler arasındaki bu ilişkiyi belirlememizde yardımcı olur ve bu sayede yeni veriler tahmin etmiş oluruz.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Veri setimizi import ediyoruz ayraç olarak noktalı virgül olduğu için bunu belirtiyoruz.
df = pd.read_csv('multilinearregression.csv', sep=';')

# linear regression modeli tanımlıyoruz:
reg = linear_model.LinearRegression()
# ilk verilenler independent değişken  daha sonra dependet değişkenler verilir
reg.fit(df[['alan', 'odasayisi', 'binayasi']], df['fiyat'])

# prediction yapalım

reg.predict([[275, 3, 11]])
# katsayıları gösterir
coef = reg.coef_
# sabir değerleri hesaplar
intercept = reg.intercept_

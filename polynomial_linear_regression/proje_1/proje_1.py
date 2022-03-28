# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:16:11 2022

@author: kundakci
"""

# Polynomial Linear Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Veri setimizi pandas yardımıyla alıp dataframe nesnemiz olan df 'in içine aktarıyoruz...
df = pd.read_csv('polynomial.csv', sep=';')

# Bir adet polynomial  regression nesnesi oluşturması için PolynomialFeatures fonksiyonunu çağırıyoruz...
# Bu fonskiyonu çağırırken polinomun derecesini (N) belirtiyoruz:
polynomial_regression = PolynomialFeatures(degree=5)
x_polynomial = polynomial_regression.fit_transform(df[['deneyim']])


# regression model nesnemizi olan reg nesnemizi oluşturup bunun fit metonu çağırarak x_polynomial ve y eksenlerini fit ediyor
# yani regresyon modelimizi mevcut gerçek verilerle eğitiyoruz:
reg = LinearRegression()
reg.fit(x_polynomial, df['maas'])

# model görselleştirme
y_head = reg.predict(x_polynomial)
plt.plot(df['deneyim'], y_head, color='red', label='polynomial regression')
plt.legend()
plt.scatter(df['deneyim'], df['maas'])
plt.show()


x_polynomial1 = polynomial_regression.fit_transform([[4.5]])
reg = reg.predict(x_polynomial1)

# #### Alacağı maaş çok güzel bir şekilde şirket politikasına fit etmiş oluyor hakkı yenmeden ! :)

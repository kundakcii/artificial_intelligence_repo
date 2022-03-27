# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:26:25 2022

@author: kundakci
"""

# OUTLİNER (AYRIK DEĞER) TESPİTİ VE VERİSETİNDEN TEMİZLEME İŞLEMLERİ
# Outliner,bir veriseti içerisindeki diğer göözlemlerden aykırı ve sapan gözlem veya veri değeridir.
import pandas as pd
df = pd.read_csv("outlier_ornek_veriseti.csv", sep=";")
describe = df.describe()
# Q1 (%25 percentile hesaplama)
Q1 = df.boy.quantile(0.25)
# Q3 (%75 percentile hesaplama)
Q3 = df.boy.quantile(0.75)
# IQR değerinin bulunması
IQR_degeri = Q3-Q1
# Alt limit üst limit hesaplama
alt_limit = Q1-1.5*IQR_degeri
ust_limit = Q3-1.5*IQR_degeri
# Meadin bulunması
Q2 = df.boy.quantile(0.50)

# Verisetindeki outler(Aykırı) değerleri bulma
aykiri_degerler = df[(df.boy < alt_limit) | (df.boy > ust_limit)]

# outlier Değerlerin veri setinden çıkarılması
# şartlar yukardakinin tam tersi
df_filtrelenmis = df[(df.boy > alt_limit) & (df.boy < ust_limit)]

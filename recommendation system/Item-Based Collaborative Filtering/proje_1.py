# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:27:53 2022

@author: kundakci
"""

import numpy as np
import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('users.data', sep='\t', names=column_names)
print(len(df))

movie_titles = pd.read_csv('movie_id_titles.csv')
print(movie_titles.head())
print(len(movie_titles))


df = pd.merge(df, movie_titles, on='item_id')

# RECOMMENDATION SİSTEMİNİ KURMA...

# Stunlarda film isimleri olacak şekilde ayarlıyoruz...
moviemat = df.pivot_table(index='user_id', columns='title', values='rating')
print(moviemat.columns)
print(moviemat.head())
print(type(moviemat))


# star wars filminin user ratinglerine bakalım

starwars_user_ratings = moviemat['Star Wars (1977)']

# corrwith() methodunu kullanarak starwars filmi ile korelasyonları hesaplatalım.

smilar_to_starwars = moviemat.corrwith(starwars_user_ratings)


# Nan dataları temizlenmesi

corr_starwars = pd.DataFrame(smilar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)

# Elde edilen dataframe' i sıralayım ve gözlemleyelim starwars 'a en yakın tavsiye edeceği film neymiş

head_of_corr_starwars_sort = corr_starwars.sort_values(
    'Correlation', ascending=False).head(10)


# Göründüğü üzere alakasız sonuçlar çıktı.Bunun nedeni starwars'  sa oy veren çok az sayıda insanın alaksız bir filme de yüksek puan vermesi.Yani aslında 10 kişi stawars ve starwars ile alakalı olmayan bir aşk filmine tam puan vermiş ve model bu ikisini aynı katagoreiye koyuyor.Gerçek verilere bakılıdğında starwars izleyicisinin beğeneceği bir film değil peki bunun üstesinden nasıl geleceğiz.

# Bu durumun üstesinden starwars izleyicisinin oyladığı ama 100 den az oy alan filmleri modelimize dahil etmeyerek aşabilir.

df.drop(['timestamp'], axis=1)

# her filmin ortalama (mean value) rating değerini bulalım
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
# Büyükten küçüğe doğru sıralayalım
sorted_ratings = ratings.sort_values('rating', ascending=False).head()


# ortalama alırken kaç oy aldığına bakmadık bu yüzden gene alakasız sonuçlar çıktı
ratings['rating_oy_sayisi'] = pd.DataFrame(
    df.groupby('title')['rating'].count())

sorted_ratings2 = ratings.sort_values(
    'rating_oy_sayisi', ascending=False).head()


# corr_starwars dataframe 'imize rating_oy_sayisi sütunu ekleyelim(join ile)

corr_starwars = corr_starwars.join(ratings['rating_oy_sayisi'])
sonuc = corr_starwars[corr_starwars['rating_oy_sayisi']
                      > 100].sort_values('Correlation', ascending=False)

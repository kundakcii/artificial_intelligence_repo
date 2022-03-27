

import pandas as pd

df_imdb = pd.read_csv('imdb_top_1000.csv')

df_head = df_imdb.head(5)

# Dataframe ' in bir kopyasını copy() kullanarak oluşturabiliriz.
df_kopya = df_imdb.copy()

#   COLUMN DROP
# dataframe 'in bazı sütunları işimize yaramayabilir
# axis=1 ise column drop, 0 ise row drop edilir. default=0
df_new = df_imdb.drop(['Overview', 'Meta_score'], axis=1)
df_new_head = df_new.head()


# yukarıda ki aynı işlemin farklı tarzda yapılması burada axis değeri atamamıza gerek yok
df_new_2 = df_imdb.drop(columns=['Overview', 'Meta_score'])
df_new_2_head = df_new_2.head()


#   ROW DROP
# row slindiği zaman indexlerde kayma olmaz 1. index silindiği zaman 0-2-3 şeklinde gider
df_new_3 = df_imdb.drop([1])
df_new_3_head = df_new_3.head()


#   FİLTERİNG
df_filtered = df_imdb[df_imdb['IMDB_Rating'] >= 9]
# veya...
df_filtered_query = df_imdb.query('IMDB_Rating >= 9')


# her sütünün hangi tipde veri  öğrenmek için
columns_types = df_imdb.dtypes

# obje olarak verilen veriden belirli bir veriyi ayırma tipini değiştirme ve var olan dataframe ekleme


def f(x): return (x["Runtime"].split())[0]


df_imdb["RuntimeNew"] = df_imdb.apply(f, axis=1)
df_imdb['RuntimeNew2'] = df_imdb['RuntimeNew'].astype('int')

df_filtered = df_imdb.query('RuntimeNew2 >= 140')










import pandas as pd

# dosya okuma ve dataframe olarak içeri alma
df_imdb = pd.read_csv("imdb_top_1000.csv")
# ilk 5 satırın gösterimi
head = df_imdb.head(5)

# son 10 satırını gösterimi
tail = df_imdb.tail(10)

# DataFrame ' in boyutlarını görebilme
imdb_shape = df_imdb.shape

# dataframe 'in baişlıklarını alma
columns_df = df_imdb.columns


# dataframe' in veri tipini gösterir
df_type = df_imdb.dtypes

# null verileri gösterir
df_null_data = df_imdb.isnull()


# sadece ilgili sütünu çağırmak için
column_series_title = df_imdb['Series_Title']

# ilgili sütünnun ilk beş kaydı
five_column_series_title = df_imdb['Series_Title'][:5]

# birden fala sütunu gösterme atandığı değişkeni dataframe yapar.
df_many_column = df_imdb[["Series_Title", "Released_Year"]]

# sıralama yapar atandığı değişkeni Dataframe yapar.
sorting = df_imdb.sort_values('Released_Year')

# hangi yılda kaçtane veri var.
year_cour = df_imdb['Released_Year'].value_counts()

# belirli indeskteki veri çekme
data_on_index = df_imdb['IMDB_Rating'][1]
# loc lokasyon
# data setinde yerini bilinmeyen datayı çekme. Daataframe döner.
any_index_of_data = df_imdb.loc[df_imdb['Series_Title'] == 'The Godfather']

# data setindeki yeri bilinmeyen datanın istediğimiz bir sütununu çekme. Dataframe döner.
any_index_of_data_on_column = df_imdb.loc[df_imdb['Series_Title']
                                          == 'The Godfather']['IMDB_Rating']

# IMDB Ratingleri 8 in üstünde olan ve No_of_Votes 100000
rating_and_no_of_vates_data = df_imdb.loc[(
    df_imdb['IMDB_Rating'] >= 8) & (df_imdb['No_of_Votes'] >= 100000)]

df_type = df_imdb.dtypes
# burada Gros ve IMDB_Rating sütünlerının data tiplerine bakınca Gros sütünun bir obje IMDB_Rating sütnu ise float türündedir
# Gros sütununa bakılınca virgül içerdiği görülür sütunun virgüllerden kurtarılması gerekir.
df_imdb['Gross'] = df_imdb['Gross'].str.replace(",", "")
# Dtanın numeric hale getirilmesi gerekir
df_imdb['Gross'] = pd.to_numeric(df_imdb['Gross'])
new_gross_type = df_imdb['Gross'].dtypes
# IMDB_Rating değeri 8 in üstünde olan ve Gross değeri (yani gişe hasılatı)30000000'dan çok olan filmleri gösterme
imdb_and_gross=df_imdb.loc[(df_imdb['IMDB_Rating']>=8.0)&(df_imdb['Gross']>50000)]



<center><h1><b>IMDB Metin Tanıma</b></h1></center>
<br>
Merhaba. Bu projede IMDB internet sitesinden çekilen yorumların olumlu yada olumsuz olarak etiketlenmiş yorumlar ile çalıştık.
</br>
<ul>
    <li>
        İlk olarak Veri setimizi yükledik
    </li>
    <li>
        Daha sonra veri setimizin içindeki yorumların içinde bulunan html tag' larini BeautifulSoup kullanarak temizledik.
    </li>
    <li>
        Daha sonra regex yardımıyla yorumların içindeki noktalama işaretlerini ve numaraları temizledik.
    </li>
    <li>
        Daha sonra Makine öğrenimi algoritmaları büyük harf ile başlayan kelimleri farklı bir kelime olarak algıladığı için bütün kelimleri küçük harfe çeviriyoruz.
    </li>
    <li>
       Daha sonra stopwords (the, am, is, are vs.) gibi kelimlerin grammer kelimeleri olduğu için tek başlarına bir anlamı yoktur bu yüzden bu kelimleri datasetimizden temizliyoruz.
    </li>
     <li>
       Datasetimizi train ve test olarak böldükten sonra...
    </li>
     <li>
        CountVectorizer kullanarak bag of words oluşturuyoruz burada ki her bir kelime bir feature olacak. max_feature sayısını biz belirliyoruz.
    </li>
    <li>
        roc_auc_score kullanarak modelimizin doğruluk oranını tahmin ediyoruz.
    </li>
</ul>
<br>
yukarıda adım adım yapılan işlemlerden bahsettim bu projeyi bir çok şekilde uyarlama yapabilirsiniz herkese iyi günler diliyorum...
</br>

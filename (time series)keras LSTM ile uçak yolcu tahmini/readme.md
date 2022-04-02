Fisher Faces<center><b><h1>Keras LSTM ile time series projesi</h1></b></center>
<br>
Bu projede LSTM derin öğrenme modelini kullanacağız.Long-Short Term Memory olarak adlandırılan LSTM ağı, zaman içerisinde geri yayılım kullanılarak eğitilen ve vanishing gradient sorunun üstesinden gelen tekrarlı bir sinir ağırıdır.
</br>
<h1></h1>
<h1>Time series nedir ?</h1>
<br>
Zamana göre sıralanmış gözlem değerlerinden oluşan veriye zaman serisi denir.yani düzenli zaman aralıklarında, ardışık zaman alanlarında tipik olarak ölçüm yapan algoritmalara denir. Ekonometride zaman serisi tahminine bir örnek, önceki başarımlarına (performanslarına) bakarak bir hisse senedinin açılış fiyatını öngörmektir.
</br>
<h2>
Time series 'de doğru tahminde bulunmak için 4 temel özelliğin kontrol edilmesi önemlidir.
</h2>
<ol type="1">
<li>
<b>
    Autocorrelation (OTOKORELASYON)
</b>
    <ul>
        <li>
        Otokorelasyon, ya da öz ilinti, bir sinyalin farklı zamanlardaki değerleri arasındaki korelasyonudur. Başka bir deyişle, gözlemlenen değerler arasındaki benzerliğin, zamansal gecikmenin bir fonksiyonu olarak ifadesidir. Otokorelasyon analizi tekrar eden örüntülerin tanınması, bir sinyalin kayıp temel frekansının tespit edilmesi gibi amaçlar için kullanılan bir matematiksel araçtır. 
        </li>
    </ul>
</li>
<li>
<b>
    Seasonality (MEVSİMSELLİK)
</b>
 <ul>
        <li>
      Zaman serisinin belirli bir davranışı belirli periyotlarla tekrar etmesi durumuna ‘mevsimsellik’ denir. Örnek bir kanalda izlenen dizinin haftanın belirli günleri eğilim olarak kendini tekrarlaması.denilebilir.
        </li>
    </ul>
</li>
<li>
<b>
    Stationarity (DURAĞANLIK)
</b>
 <ul>
        <li>
      Zaman serisi modeli yapmak istenildiğinde, üretilen stokastik sürecin zamana bağlı olarak değişip değişmediği incelenmelidir. Zamana göre değişen bir özellik varsa seri durağan değildir. Durağan olmayan zaman serilerinin matematiksel formatta bir model yazılması mümkün değildir.Otokorelasyon, bir varlığın mevcut değerleri ile geçmiş değerleri arasındaki ilişkiyi belirlemeye yardımcı olur.
        </li>
        <li>
         Bir zaman serisinin durağanlığı, KPSS testi, Dickey-Fuller testi gibi testler ile kontrol edilebilir.
        </li>
    </ul>
</li>

<li>
<b>
    Trends
</b>
 <ul>
        <li>
    Trendler uzun bir süre boyunca kaydedilir. Varlığın doğasına ve ilgili etkileyen faktörlere bağlı olarak, eğilimi azalabilir, artabilir veya sabit kalabilir. Örneğin nüfus, doğum hızı, ölüm hızı vb. en çok hareket gösteren ve bu nedenle durağan bir zaman serisi oluşturamayan varlıklardan bazılarıdır.
        </li>
    </ul>
</li>
</ol>

<h1>Modelling Time Series Data</h1>
<ul>
<li>
<b>Hareketli Ortalama (MA)</b> yöntemi, tüm zaman serisi tahmin modellerinin en basit ve en temel olanıdır.Bir MA modelinde, çıktı (veya gelecek) değişkeninin mevcut ve geçmiş değerlere doğrusal bir bağımlılığa sahip olduğu varsayılır. Böylece geçmiş değerlerin ortalamasından yeni seri oluşturulur.
</li>
<li>
<b>Üstel Düzeltme (ES)</b> yöntemi, popüler zaman serisi tahmin modellerinden biridir. MA yöntemi gibi ES tekniği de tek değişkenli seriler için kullanılmaktadır. Burada yeni değerler, geçmiş değerlerin ağırlıklı ortalamasından hesaplanır. Bir değer ne kadar eskiyse, ona atanan ağırlık o kadar az olur. Değişkenin eğilimlerine ve mevsimselliğine göre basit (tekli) ES yöntemini veya gelişmiş (ikili veya üçlü) ES zaman serisi modelini kullanabilirsiniz.
<ol type='I'>
<li>
Holt-Winters Üstel Düzeltme olarak da bilinen üçlü üstel teknik, verilerdeki eğilim ve mevsimsellik nedeniyle üç düzeyde düzeltme içerir. Dolayısıyla, α ve β faktörünün yanı sıra, bu yöntem serideki mevsimselliğin etkisini kontrol etmek için bir gama (γ) parametresini içerir.
</li>
</ol>
</li>
<li>
Otoregresif Entegre Hareketli Ortalama (ARIMA) modeli, iki veya daha fazla zaman serisi modelinin kombinasyonunu içeren, yaygın olarak kullanılan bir başka tahmin tekniğidir. Bu model, çok değişkenli durağan olmayan veriler için uygundur. ARIMA yöntemi, otoregresyon, otokorelasyon ve hareketli ortalama kavramlarına dayanmaktadır.
<ol type='I'>
<li>
SARIMA (Mevsimsel ARIMA), temel olarak zaman serilerinin mevsimsel unsurunu dikkate alan ARIMA'nın bir uzantısıdır.
</li>
</ol>
</li>
</ul>


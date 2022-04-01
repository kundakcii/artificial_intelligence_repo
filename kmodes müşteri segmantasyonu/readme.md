<center><h1><b>kmodes Kullanarak Müşteri Segmantasyonu</b></h1></center>
<br>
Daha öncede k-means kullanarak müşteri segmantasyon örneği yapmıştık ama daha küçük çaplı bir örnekti. <a href="https://github.com/kundakcii/artificial_intelligence_repo/tree/main/k-means%20clustering">Örnek burada</a>.
</br>
<br>
Bu projede ise Kmodes Clustering kullanacağız.Peki nedir bu Kmodes clustering.
</br>
<h1></h1>
<h2>
KModes Clustering
</h2>
<br>
KModes Clustering, kategorik değişkenleri sınıflandırmak için kullanılan denetimsiz Makine Öğrenimi algoritmalarından biridir.
</br>
<h2>
KMeans vs Kmodes
</h2>
<ul>
<li>
KMeans algoritması verileri sınıflandırmak için matematiksel ölçüleri(mesafeyi) baz alır. mesafe ne kadar azsa veri noktaları o kadar benzer olur.Centroid 'ler Means tarafından güncellenir.
</li>
<li>
Ancak kategorik veri noktaları için mesafe hesaplamak mantıklı olmaz.Bu yüzen KModes kullanırız. Veri noktaları arasındaki farklılıkları kullanır ve farklılıklar ne kadar azsa veri noktalarımız o kadar benzer olurlar.Ortalama yerine verilerin mod değerlerinden yararlanır.
</li>
</ul>

<h1>Projede Ne Yaptık</h1>
<ul>
<li>
veri setimizi okuduktan sonra ilk olarak kullanmıyacağımız veya ilerde kullanacağımız verilerimizi ayrıştırdık.
</li>
<li>
KModes Clustering yaparken sadece float veriler ile çalışıldığı için int olan verilerimiz float haline çevirdik.
</li>
<li>
Daha sonra modelimizi oluşturduk ve hangi featurların kategorik değer taşıdığını modelimize söyledik.
</li>
<li>
son olarak modelimizin oluşturduğu sınıflandırmaya ait bazı verileri görselleştirdik...
</li>
</ul>
<img  width="500" height="600" src="https://github.com/kundakcii/artificial_intelligence_repo/blob/main/kmodes%20m%C3%BC%C5%9Fteri%20segmantasyonu/Figure%202022-04-01%20171141.png" alt="Age-Income graph" >
<img  width="500" height="600" src="https://github.com/kundakcii/artificial_intelligence_repo/blob/main/kmodes%20m%C3%BC%C5%9Fteri%20segmantasyonu/Figure%202022-04-01%20173035.png" alt="Education-Income graph" >

<br>
Herkese iyi günler...
</br>

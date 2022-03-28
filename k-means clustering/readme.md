<center><h1><b>K-MEANS CLUSTERİNG</b></h1></center>

<ul>
      <li>
      Çok fazla sayıda ham veriyi gruplamak için kullanılır.
      </li>
      <li>
      Ham veriler hakkında önceden bir sınıflandırmaya ihtiyaç duymaz
      </li>
      <li>
      Unsupervised Learning modellerinden en yaygın kullanılanıdır.Temel bir modeldir.
      </li>
</ul>
<center><h1></h1></center>
<ul>
    <li>
    Ham datayı gruplamak için önce kaç adet grup kullanacağını siz algoritmaya söylemeniz lazım 
    </li>
    <li>
    K-Means kelimesinde ki <b>K</b> => <b>K adet centroidi </b> ifade eder
    </li>
</ul>
<h1></h1>
<center>
    <h2>
        <b>
            K-MEANS ALGORİTMASININ ÇALIŞMA ŞEKLİ
        </b>
    </h2>
</center>

<ol type="1">
  <li> 
    K adet centroid (Merkez Nokta) seçilir.
  </li>
   <li> 
    Her veri rastgele gruplara konur ve aynı grupta olan verilerin centroid merkezleri hesaplanır.
  </li>
  <li>
    Her veriyi (noktayı) kendine en yakın centroid grubuna dahil eder.
  </li>
  <li>
    Her centroidin merkezini kedni grubundaki noktalara bakarak tekrar hesaplar ve centroidi yeni merkez lokasyona koyar.
  </li>
  <li>
    <br/>1. ve 3. adım centroidler artık yer değiştirmeyene kadar devam eder.ve gruplamayı bitirir.
  </li>
</ol>
<h1></h1>
<center>
    <h2>
        <b>
            K DEĞERİNİ BELİRLERKEN
        </b>
    </h2>
</center>
<ul>
    <li>
   K değeri belirlenirken The Elbow Method yada The Silhouette Method kullanılır. K değerleri distorrion değerleri ile birlikte grafiğe döktüğünüzde dirsek noktası bulunan k değeri en optimal k değeri olarak kabul edilir 
    </li>
</ul>
<h3>
    <b>
        The Elbow Method
    </b>
</h3>
<p>
En uykun küme sayısını belirlerken uygulanan en bilinen yöntemdir.
</p>
<ul>
    <li>
        datanın centroid merkezinden uzaklığının karesi her data için hatanın karesidir.
    </li>
    <li>
    WSS puanı, tüm puanlar için bu kareli hataların toplamıdır
    <ul>
        <li>
        Öklid Mesafesi veya Manhattan Mesafesi gibi herhangi bir mesafe metriği kullanılabilir.
        </br>
        ayrıca
        <a href="https://github.com/kundakcii/artificial_intelligence_repo/tree/main/KNN">uzaklık algoritmaları</a> ' na bakabilirsiniz.
</li>
    </ul>
    </li>
    <li>
    K değeri 2 tam sayı arasında yada birden fazla değer çıkıyorsa <b>The Silhouette Method</b> ' na başvurulabilir.
    </li>
</ul>
<h1></h1>
<h3>
    <b>
        The Silhouette Method
    </b>
</h3>
<p>
kısace Siluet değeri, bir noktanın diğer kümelere kıyasla kendi kümesine ne kadar benzer olduğunu ölçer.
</p>
<ul>
    <li>
    silhouette değeri 1 ile -1 arasındadır.
    </li>
    <li>
    Birçok noktanın Silhouette değeri negatifse, çok fazla veya çok az küme oluşturduğumuzu gösterebilir
    </li>
    <li>
    Siluet Puanı, optimal k'de global maksimum değerine ulaşır.
    </li>
    <li>
    optimum K Silhouette Value-versus-k grafiğinde bir tepe noktası olarak görünmelidir.
    </li>
</ul>
<br>
The Elbow Method daha çok bir karar kuralıdır, Silhouette ise kümeleme sırasında doğrulama için kullanılan bir ölçümdür. Böylece Dirsek Metodu ile birlikte kullanılabilir.
<<<<<<< HEAD
</br>
=======
</br>
>>>>>>> 6d5bb5de914e4b02dcb0ac17c504d603c095fd9a

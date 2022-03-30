<center> 
    <h1>
        <b>
        Recommendation System
        </b>
    </h1>
</center>
<h2>1. User-Based Collaborative Filtering</h2>
<h1></h1>
<ul>
    <li>
    kullanıcılar arsindeki benzerlik skorlarını bulmaya çalışır.
    </li>
    <li>
    her bir kullanıcının satın aldığı veya izlediği/kullancıdığı metaryeli kullanıcı bazlı olarak tutar ve bir matrise dönüştürür.
    </li>
    <li>
    bir kullanıcıya benzer başka kullanıcılar bulur.
    </li>
    <li>X kullanıcısının henüz izlemediği ancak benzer kullanıcıların çoğunun izlediği bir film varsa bunu X kullanıcısına önerir
    </li>
</ul>
<h3>DEZAVANTAJLARI</h3>
<ul>
    <li>
   Kullanıcı bazlı olduğu için maliyetlidir. insan sayısı film sayısı her zaman fazladır.
    </li>
    <li>
        İnsan zevkleri değişebilir bugün sevdiğini yarın sevmeyebilir.
    </li>
    <li>
    bir kullanıcıya benzer başka kullanıcılar bulur.
    </li>
    <li>X kullanıcısının henüz izlemediği ancak benzer kullanıcıların çoğunun izlediği bir film varsa bunu X kullanıcısına önerir
    </li>
</ul>
<h2>2. Item-Based Collaborative Filtering</h2>
<h1></h1>
<ul>
    <li>
        User-Based collabrative filtering 'de yaşanan sıkıntıları aşmak için Item-Based method geliştirilmiştir
    </li>
    <li>
        Kullanıcılar yerine itemlerı baz alır.kullanıcılar arasındaki ilişkiyle ilgilenmez, Itemlar arasındaki ilişki ve benzerlikle ilgilenir yani birbirine benzeyen itemları bulur.
    </li>
    <li>
    Itemlar arasındaki benzerlik skorlarını bulmaya çalışır.
    </li>
</ul>

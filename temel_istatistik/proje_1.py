# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:59:32 2022

@author: kundakci
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# Random kullanarak sample bir veri setini kendimiz oluşturalım
# Aylık gelir 5000 tl standart deviation 2000 tl olsun 1000 kişinin random aylık maaşı
gelirler = np.random.normal(5000, 2000, 1000)
np_mean = np.mean(gelirler)

# matplotlib kütüphanesi kullanarak çizilmesi
plt.hist(gelirler, 100)
plt.show()
# Median bulunması
np_median = np.median(gelirler)
# varyans hesaplama
gelirler_varyans = gelirler.var()
# standatr sapmanın hesaplanması
gelirler_std = gelirler.std()
# Herşey iyi diyelimki elimizde hatalı uçuk bir veri var
gelirler = np.append(gelirler, [100000000])

np_mean = np.mean(gelirler)
np_median = np.median(gelirler)
# mean ve median arasında çok uçuk farklar varsa veri seti incelenmelidir.

# Mode:
# Bir okuldaki çocukların ortalama yaş değerleri random oluşturalım, Toplam 300 öğrenci, yaşlar 7 ile 18 arasında

yaslar = np.random.randint(7, 18, size=300)
stats.mode(yaslar)
# stats kütüphanesinin incelenmesinde yarar var
yaslar_median = np.median(yaslar)
yaslar_mean = np.mean(yaslar)

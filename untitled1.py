# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:05:34 2022

@author: kundakci
"""

import numpy as np
a = np.array([1, 5, 10])
print(a)

b = np.array([[1, 7, 20], [5, 8, 9]])

# Dizinin boyutunu ğrenmek için endim
boyut_b = b.ndim
boyut_b = a.ndim
# boyutunu ööğrenmek için
shape_b = b.shape
# tipini ööğrenmek için
dtype_b = b.dtype

print(b[0])
print(b[1][0])
print(b[0, 1:])

# otamatik dizi oluşturmak
# tümü sıfır matrix dizisi
disi_s = np.zeros((2, 3))

# bütün elemanları aynı değer olan dizi
dizi1 = np.full((4, 4), 50)


# Random dizi oluşturmak
dizi2 = np.random.rand(4, 3)
# belirli biraralıkta verme
dizi3 = np.random.randint(0, 100, size=(5, 5))


# DİZİ KOPYALARKEN DİKKAT
a = np.array([1, 2, 3])
b = a
b[0] = 90

print(a)

# b bir pointer gibi a' nın gösterdiği aynı memory lokasyonunu gösterir o nedenle b de yapılan bir değişiklik a ' yı da etkiler
# bu tarz durumlarla karşılaşmamk için copy() fonksiyonunu kullanmlaıyız.

a = np.array([2, 3, 4])
b = a.copy()
b[0] = 90
print(a)
print(b)

# dizilerde matematiksel işlemler
a = np.array([1, 2, 3, 4])
a = a+4
a = a*2
a = a/2
b = np.array([1, 0, 1, 0])
a = a+b
a = a**2

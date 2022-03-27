import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.show()

plt.title('İlk Grafiğim..!')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# çentik koyma
plt.xticks(x)
plt.yticks(y)
plt.plot(x, y)
plt.show()

# lejant koyma ve grafiği özelleştirme
plt.plot(x, y, label='x^2', color='green',
         linewidth=2, linestyle='--', marker='.')
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([1, 4, 9, 16, 25])
plt.title('İlk Grafiğim')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()


# aynı grafikte birden fazla çizim yapma
plt.plot(x, y, label='x^2', color='green',
         linewidth=2, linestyle='--', marker='.')
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 1, 4, 9, 16, 25])
plt.title('İlk Grafiğim..!')
plt.xlabel('X axis')
plt.ylabel('Y axis')


# 2.grafiğin çizilmesi
x2 = np.arange(0, 5, 0.5)
plt.plot(x2, x2*2, color='red', linewidth=2, marker='.', label='2*x5')


# grafiği bilgisayara kaydetme

plt.savefig('ilk_grafiğim.png', dpi=300)
plt.show()


#   BARCHART
x = ['Ankara', 'İstanbul', 'İzmir']
y = [120, 178, 87]
plt.bar(x, y)
plt.show()

# Eğer çubuklardan birini özelleştirmek isterseniz

cubuklar = plt.bar(x, y)
cubuklar[1].set_hatch('/')
cubuklar[0].set_hatch('.')
plt.show()


# Detaylı örnekler
gas = pd.read_csv('petrolfiyatlari.csv')
plt.title('PEtrol Fiyatları')
plt.plot(gas['Year'], gas['USA'], '-b', label='USA')
plt.xlabel('Yıl')
ply.ylabel('Dolar')
plt.lengend()
plt.show()
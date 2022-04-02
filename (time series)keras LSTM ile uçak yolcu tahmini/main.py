# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 01:50:42 2022

@author: kundakci
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('AirPassengers.csv')

df.rename(columns={'#Passengers': 'passengers'}, inplace=True)
df = df['passengers']
print((type(df)))


# Tip olarak ya Dataframe olacak yada numpy array olacak
df = np.array(df).reshape(-1, 1)
print(type(df))

# datanın çizilmesi
plt.plot(df)
plt.show()


# SCALING IŞLEMI...
scaler = MinMaxScaler()
df = scaler.fit_transform(df)
train = df[0:100, :]
test = df[100:, :]

#


def get_data(data, steps):
    dataX = []
    dataY = []
    for i in range(len(df)-steps-1):
        a = df[i:(i+steps), 0]
        dataX.append(a)
        dataY.append(df[i+steps, 0])
    return np.array(dataX), np.array(dataY)


steps = 2

x_train, y_train = get_data(train, steps)
x_test, y_test = get_data(test, steps)

# LSTM kullanarak reshaping işlemi
x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))
x_test = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))


model = Sequential()
model.add(LSTM(128, input_shape=(1, steps)))
model.add(Dense(64))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()

# Şimdi modelimiz deneyelim...
model.fit(x_train, y_train, epochs=25, batch_size=1)

# prediction yapma zamanı...
y_pred = model.predict(x_test)

y_pred = scaler.inverse_transform(y_pred)
y_test = y_test.reshape(-1, 1)
y_test = scaler.inverse_transform(y_test)


# verilerimizi çizdirme zamanı...
plt.plot(y_test, label='real number of passengers')
plt.plot(y_pred, label='predict number of passenger')
plt.ylabel('Months')
plt.xlabel('Number of passengers')
plt.legend()
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:38:22 2022

@author: kundakci
"""

import numpy as np
from PIL import Image
from IPython.display import Image as show_image
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input, decode_predictions

img = Image.open('car.jpg').resize((299, 299))

img = np.array(img)
print(img.shape, 'görüntümüz 3 boyutlu with,heigh,color')

# kullanacağımız model 4 boyutlu istiyor
img = img.reshape(-1, 299, 299, 3)
print(img.shape)

# scale etme işlemi
img = preprocess_input(img)


incresv2_model = InceptionResNetV2(weights='imagenet', classes=1000)
print(incresv2_model.summary())
print(type(incresv2_model))
show_image(filename='car.jpg')

preds = incresv2_model.predict(img)
print('Predicted categories: ', decode_predictions(preds, top=2)[0])

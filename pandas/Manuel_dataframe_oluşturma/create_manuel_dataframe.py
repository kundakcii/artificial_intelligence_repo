# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:17:04 2022

@author: kundakci
"""

import random

random_list_1 = random.sample(range(15, 25), 2)
random_list_2 = random.sample(range(15, 25), 2)
random_list_of_lists = [random_list_1, random_list_2]

columns=['Sıcaklık 1.gün','Sıcaklık 2.gün']
myDataframe _ pd.Dataframe(random_list_of_lists,index=['İst','Ankara'],columns=columncolumns)


type(myDataframe)

type(df)

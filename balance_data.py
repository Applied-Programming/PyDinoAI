# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('final_training_data.npy')


df = pd.DataFrame(train_data)
print(len(train_data))
print(df.head())
print(Counter(df[1].apply(str)))

"""
straights = []
ups = []
downs = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0]:
        straights.append([img,choice])
    elif choice == [0,1,0]:
        ups.append([img,choice])
    elif choice == [0,0,1]:
        downs.append([img,choice])
    else:
        print('no matches')


forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]

final_data = forwards + lefts + rights
shuffle(final_data)

np.save('training_data.npy', final_data)
"""

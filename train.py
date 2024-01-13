#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('data/spotify.csv')

df = df.drop(["Unnamed: 0", "track_id"], axis = 1)

df["explicit"] = df["explicit"].astype(int)
df = df.dropna() #deleting the few small null raws

strings = list(df.dtypes[df.dtypes == 'object'].index) #ottengo gli indici che hanno solo valori string
df['duration_ms'] = np.log1p(df['duration_ms'])

for col in strings: #loop per ogni colonna
    df[col] = df[col].str.lower()

# # Splitting the Data
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=11)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=11)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_full_train = df_full_train.reset_index(drop=True)

y_train = df_train.popularity
y_val = df_val.popularity
y_test = df_test.popularity
y_full_train = df_full_train.popularity

del df_train['popularity']
del df_val['popularity']
del df_test['popularity']
del df_full_train['popularity']

def rmse(y, y_pred):
    error = y - y_pred #calcolo errore tra i 2 array
    se = error **2 #quadrato della differenza
    mse = se.mean() #media della differenza
    return np.sqrt(mse) #radice del valore medio


#train
train_dicts = df_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)
#val
val_dicts = df_val.to_dict(orient='records')
X_val = dv.transform(val_dicts)
#ft train
dicts_ft = df_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(dicts_ft)
#test
dicts_test = df_test.to_dict(orient='records')
X_test = dv.transform(dicts_test)


model = DecisionTreeRegressor( max_depth=None, min_samples_leaf=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_val)
_rmse = rmse(y_val, y_pred)

print(_rmse)

output_file = 'song_model.bin'
with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)
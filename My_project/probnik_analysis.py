# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:19:14 2018

@author: Sony VAIO Pro
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns 
import matplotlib.pyplot as plt

#Read csv
df = pd.read_csv("blyads_prob.csv", encoding='cp1251')
print(df.columns)

#Group by data type
df.columns.to_series().groupby(df.dtypes).groups

df['chas'] = pd.to_numeric(df['chas'], downcast='float', errors='coerce')
df['dva_chasa'] = pd.to_numeric(df['dva_chasa'], downcast='float', errors='coerce')
df['noch'] = pd.to_numeric(df['noch'], downcast='float', errors='coerce')
#df['ves'] = df['ves'].str[5:]
df['ves'] = pd.to_numeric(df['ves'], downcast='float', errors='coerce')
#df['rost'] = df['rost'].str[6:]
df['rost'] = pd.to_numeric(df['rost'], downcast='float', errors='coerce')
#df['vozrast'] = df['vozrast'].str[9:]
df['vozrast'] = pd.to_numeric(df['vozrast'], downcast='float', errors='coerce')
#df['razmer'] = df['razmer'].str[7:]
df['razmer'] = pd.to_numeric(df['razmer'], downcast='float', errors='coerce')
#df['vpopu'] = df['vpopu'].str[5:]


df['backdoor'] = df['vpopu']
#Replace extra proces with '1'
df.loc[df['vpopu'] > 1] = 1
df.loc[0 == df['backdoor']] = 'nan'
df.loc[1 == df['backdoor']] = '0'
df['backdoor'] = pd.to_numeric(df['backdoor'], downcast='float', errors='coerce')

'''
    df.backdoor.value_counts(normalize=False, sort=True,
                             ascending=False, bins=None, dropna=True)


'''
print(df.tail())
#################################################################

'''
corrmat2 = df.corr()
#f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat2,linewidths=.1)
'''
################################################################

'''

x = df.isnull().sum()
x_ascend = x.sort_values(ascending = [False])
x_asc_df = pd.DataFrame(x_ascend)


#Number of variables with missing values.
np.count_nonzero(x_asc_df)

x_asc_df[0:53]

#Imputing prices with their means
df = df.fillna(df.mean()['chas':'noch'])


corrmat2 = df.corr()
#f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat2,linewidths=.1)

#################################################################

df.head()


from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept = True)

model.fit(df.chas[:, np.newaxis], df.dva_chasa)

xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])

plt.scatter(df.vpopu, df.ves)




############################################

from sklearn.linear_model import LogisticRegression

x = df['chas'].dropna()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        x, df['vpopu'][:2774], random_state=0)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))

print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

dataframe = pd.DataFrame(X_train)

grr = pd.scatter_matrix(dataframe, c=y_train, figsize=(15, 15), marker='o',
                        hist_kwds={'bins': 20}, s=60, alpha=.8)





log_reg = LogisticRegression()
log_reg.fit(x, y)

plt.plot(x, y)
    

    
'''
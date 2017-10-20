#!/usr/bin/python

import pandas as pd
from math import sqrt


def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x) * square_rooted(y)
    return round(numerator/float(denominator),3)

# For the risky asset classes that have the first differences values
df = pd.read_csv('Data/btc-world-indices-diff.csv')

n_days= df.BTC.nunique()
n_assets = df.columns.size - 1

print 'BTC to Market Indices co-relation'
print 'Number of days = ' + str(n_days) + ' | Number of Assets = ' + str(n_assets)

# Now calculating the similarites between the btc and the various market indices
for assets in df.columns.values[2:]:
    print 'Cosine Similarity between BTC and',assets,'is :',cosine_similarity(df['BTC'].values, df[assets].values)

# For the safe asset classes that have the first differences values
df = pd.read_csv('Data/btc-safe-securities-diff.csv')

n_days= df.BTC.nunique()
n_assets = df.columns.size - 1

print ''
print 'BTC to Safe Asset Classes co-relation :'
print 'Number of days = ' + str(n_days) + ' | Number of Assets = ' + str(n_assets)

# Now calculating the similarites between the btc and the various market indices
for assets in df.columns.values[2:]:
    print 'Cosine Similarity between BTC and',assets,'is :',cosine_similarity(df['BTC'].values, df[assets].values)

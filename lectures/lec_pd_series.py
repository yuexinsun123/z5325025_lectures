""" lec_pd_series.py

Companion codes for the lecture on pandas Series
"""

import pandas as pd


# ---------------------------------------------------------------------------- 
#   The dates and prices lists
# ---------------------------------------------------------------------------- 
dates = [
  '2020-01-02', 
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600, 
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# ---------------------------------------------------------------------------- 
#   Create a Series instance
# ---------------------------------------------------------------------------- 
# Create a series object
ser  = pd.Series(data=prices, index=dates)
print(ser)

# Select Qantas price on '2020-01-02' ($7.16) using ...

# ... the `prices` list
prc0  = prices[dates.index('2020-01-02')]
print(prc0)

# ... the `ser` series
prc1  = ser['2020-01-02']
print(prc1)

# ---------------------------------------------------------------------------- 
#   Slicing series
# ---------------------------------------------------------------------------- 
# Unlike dictionaries, you can slice a series
prcs  = ser['2020-01-06':'2020-01-10']
print(prcs)
# Using the lists:
print(prices[dates.index('2020-01-06'):dates.index('2020-01-10')+1])

# ---------------------------------------------------------------------------- 
#   Accessing the underlying array
# ---------------------------------------------------------------------------- 

# Use `.array` to get the underlying data array
ary  = ser.array
print(ary)

# Like any instance, you can get its type (i.e., the class used to create the
# instance)
print(type(ser.array))

# Use the `index` attribute to get the index from a series
the_index  = ser.index
print(the_index)

# Like any instance, you can get its type (i.e., the class used to create the
# instance).
print('The type of `the_index` is', type(the_index))

# ---------------------------------------------------------------------------- 
#   Changing the index by assignment
# ---------------------------------------------------------------------------- 

# The old index is:
#
# Index(['2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
#    '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15'],
#   dtype='object')

# Replace the existing index with another with different values
# Note the -4 and 1000  
ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000]
print(ser.index)
# The new index is:
# Int64Index([0, 1, 2, 3, -4, 5, 6, 7, 8, 1000], dtype='int64')



# ---------------------------------------------------------------------------- 
#   Selecting obs using the new index
# ---------------------------------------------------------------------------- 
# Lets see how the series looks like
print(ser)

# This will return 7.04
x  = ser[1000]
print(x)

# Compare the following cases:
# 1. This will return the element associated with the index label -4 
#    (or 6.86)
print(ser[-4])

# 2. This will return the fourth element from the end of the **list** `prices` 
#    (or 7.00)
print(prices[-4])



# Quiz
ind=['a', 'b', 'c']
val=[1, 2, 3]
series_abc = pd.Series(index=ind, data= val)

prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }
a=[]
b=[]
for key, value in prc_date.items():

    a.append(key)
    b.append(value)
series_stk = pd.Series(index=b, data= a)

# Given the dictionary
dic = {i:i+1 for i in range(10000)}
a=[]
for i in range(10000):
  a.append(i)

series_ones = pd.Series(data=1, index=a)



aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]
b=[]
c=[]
for i in range(len(aud_usd_lst)):
    a=aud_usd_lst[i]
    time,value=a
    b.append(time)
    c.append(value)
aud_usd_series = pd.Series(index=b,data=c)

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]
d=[]
e=[]
for j in range(len(eur_aud_lst)):
    f=eur_aud_lst[j]
    times,values=f
    d.append(times)
    e.append(values)
eur_aud_series = pd.Series(index=d,data=e)

df = pd.DataFrame({'AUD/USD':aud_usd_lst, 'EUR/AUD':eur_aud_lst})
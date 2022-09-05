#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 載入 NumPy, Pandas 套件
import numpy as np
import pandas as pd


# In[5]:


df = pd.DataFrame([[30,20]], columns=['apples','bananas'])
print(df)


# In[6]:


df=pd.DataFrame([[30,21],[41,34]], columns=['apples','bananas'], index=['2017 Sales','2018 Sales'])
print(df)


# In[7]:


s=[
  ['Austin', 139, 'Sun'],
  ['Dallas', 237, 'Sun'],
  ['Austin', 139, 'Mon'],
  ['Dallas', 456, 'Mon']
]

df=pd.DataFrame(s, columns=['city', 'visitor', 'weekday'])
print(df)
df


# In[8]:


for day in set(df['weekday']):
    print(day, df[df['weekday']==day]['visitor'].mean())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





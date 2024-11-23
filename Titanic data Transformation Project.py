#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import mode


# In[2]:


df = pd.read_csv(r'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv')


# In[3]:


df[0:5]


# In[4]:


df.shape


# In[5]:


df.columns.tolist()


# In[6]:


df.describe()


# In[7]:


df1 = pd.DataFrame({'column name' : df.columns.tolist(),
       'count of Na' : df.isna().sum()})
df1


# In[8]:


df['Survived'].fillna(np.median(df['Age']),inplace = True)
df


# In[9]:


df['Survived'].fillna(df['Survived'].mode(),inplace = True)
df


# In[10]:


df.isna()


# In[11]:


plt.hist(df['Age'],bins = [0,20,40,60,80,100],color='r')
plt.show()


# In[12]:


plt.hist(df['Fare'],bins = [0,20,40,60,80,100],color='r')
plt.show()


# In[13]:


plt.hist(df['Survived'],bins = [0,1],color='r')
plt.show()


# In[22]:


sns.boxplot(x=df['Sex'],y=df['Pclass'],color = 'b')
plt.show()


# In[23]:


df1 = df.corr()
df1


# In[16]:


plt.figure(figsize=(12, 6))
plt.subplot(2,2,1)
plt.scatter(df1['Age'], df1['Fare'])
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.subplot(2,2,2)
plt.scatter(df1['Age'], df1['Survived'])
plt.title('Age vs Survived')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.show()


# In[17]:


plt.plot(df1['Fare'], df1['Pclass'])
plt.title('Fare by Pclass')
plt.xlabel('Fare')
plt.ylabel('Pclass')
plt.show()


# In[18]:


def Family(row):
    if row['Siblings/Spouses Aboard'] == 0 and row['Parents/Children Aboard'] == 0:
        return 'Travelled with family'
    else:
        return 'Travelled alone'
df['Family'] = df.apply(Family, axis=1)
df


# In[20]:


df['Name Length'] = df['Name'].str.len()
df


# In[ ]:





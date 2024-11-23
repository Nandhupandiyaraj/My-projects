
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import mode


df = pd.read_csv(r'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv')



df[0:5]


df.shape

df.columns.tolist()

df.describe()

df1 = pd.DataFrame({'column name' : df.columns.tolist(),
       'count of Na' : df.isna().sum()})
df1

df['Survived'].fillna(np.median(df['Age']),inplace = True)
df
df['Survived'].fillna(df['Survived'].mode(),inplace = True)
df
df.isna()

plt.hist(df['Age'],bins = [0,20,40,60,80,100],color='r')
plt.show()

plt.hist(df['Fare'],bins = [0,20,40,60,80,100],color='r')
plt.show()


plt.hist(df['Survived'],bins = [0,1],color='r')
plt.show()

sns.boxplot(x=df['Sex'],y=df['Pclass'],color = 'b')
plt.show()


df1 = df.corr()
df1


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


plt.plot(df1['Fare'], df1['Pclass'])
plt.title('Fare by Pclass')
plt.xlabel('Fare')
plt.ylabel('Pclass')
plt.show()

def Family(row):
    if row['Siblings/Spouses Aboard'] == 0 and row['Parents/Children Aboard'] == 0:
        return 'Travelled with family'
    else:
        return 'Travelled alone'
df['Family'] = df.apply(Family, axis=1)
df

df['Name Length'] = df['Name'].str.len()
df





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

d = pd.read_csv('C:\\Users\\91810\\Desktop\\titanic.csv', sep='\t')
a = d[['Pclass', 'Age','Sex']].values
y=d['Survived'].values


plt.scatter(x=d['Age'],y=d['Fare'],c=d["Pclass"])

plt.plot([0,70],[0,30])
plt.show()
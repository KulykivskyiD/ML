import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

data=pd.read_csv('data.csv')

data[['Pclass','Fare','Age','Sex']]
clean=data[['Pclass','Fare','Age','Sex','Survived']].dropna()
test=np.asarray(clean[['Pclass','Fare','Age','Sex']])

for i in range(len(test)):
    if test[i][3]=='male':
        test[i][3]=0
    else:
        test[i][3]=1

des=np.asarray(clean['Survived'])
clf=DecisionTreeClassifier(random_state=241)
clf.fit(test,des)
importances = clf.feature_importances_
print(importances)

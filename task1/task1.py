import pandas as pd

data= pd.read_csv('data.csv', index_col='PassengerId')
data.head()
male=data['Sex'].value_counts().get('male')
female=data['Sex'].value_counts().get('female')
survived=float(data['Survived'].value_counts(1).get(1))*100
survived=round(survived,2)
firstclass=float(data['Pclass'].value_counts(1).get(1))*100
firstclass=round(firstclass,2)
mean=round(data['Age'].mean(),2)
median=data['Age'].median()
pearson=round(data['SibSp'].corr(data['Parch'],method='pearson'),2)
data['Name'].value_counts()
draft=['Miss.','Mrs.','Ms.']
miss=[]


for m in data['Name']:
    for d in draft:
        
        if m.find(d)!=-1:
            
            m=m[m.find(d)+len(d):]
            if m.find('(')!=-1:
                m=m[m.find('(')+1:m.find(')')]
                miss.append(m.split(' ')[0])
            else:    
                miss.append(m.split(' ')[1])
             
            

miss=pd.Series(miss)
miss.value_counts()

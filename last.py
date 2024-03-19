import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score

#import numpy as np


asd_data = pd.read_csv('Datasets/asd_dataset.csv',index_col=0)

asd_data['Class'].replace('No',0,inplace=True)
asd_data['Class'].replace('Yes',1,inplace=True)
asd_data['Sex'].replace('m',0,inplace=True)
asd_data['Sex'].replace('f',1,inplace=True)
asd_data['Jaundice'].replace('no',0,inplace=True)
asd_data['Jaundice'].replace('yes',1,inplace=True)
asd_data['Family_mem_with_ASD'].replace('no',0,inplace=True)
asd_data['Family_mem_with_ASD'].replace('yes',1,inplace=True)
asd_data['Who_completed_the_test'].replace('Health Care Professional','Health care professional',inplace=True)
asd_data['Who_completed_the_test'].replace('family member',0,inplace=True)
asd_data['Who_completed_the_test'].replace('Health care professional',1,inplace=True)
asd_data['Who_completed_the_test'].replace('Self',2,inplace=True)
asd_data['Who_completed_the_test'].replace('Others',3,inplace=True)


#from sklearn.model_selection import train_test_split
X = asd_data.drop('Class', axis=1)
y = asd_data['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)
#print(X_test)

from sklearn.ensemble import RandomForestClassifier
#from sklearn.metrics import classification_report,confusion_matrix

rfc = RandomForestClassifier(n_estimators=5)
rfc = rfc.fit(X_train,y_train)
predictions_rf = rfc.predict(X_test)
sum=0
for t in rfc.estimators_:
    clf=t
    #clf.fit(X_train,y_train)
    print(X_test[3:4])
    res= clf.predict(X_test[3:4])
    print(res)
    sum+=res[0]
    
print(sum)
    
acc_rf = accuracy_score(y_true=y_test, y_pred= predictions_rf)
print("Overall accuracy of ADA model using test-set is : %f" %(acc_rf*100))

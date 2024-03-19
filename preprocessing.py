import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import numpy as np


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


from sklearn.model_selection import train_test_split
X = asd_data.drop('Class', axis=1)
y = asd_data['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

rfc = RandomForestClassifier(n_estimators=600)
rfc = rfc.fit(X_train,y_train)
predictions_rf = rfc.predict(X_test) # new output as predictions_rf, actual output as y_test
acc_rf = accuracy_score(y_true=y_test, y_pred= predictions_rf)*100
print("Overall accuracy of RF model using test-set is : %f" %(acc_rf))

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
ada = AdaBoostClassifier(n_estimators=500)
ada.fit(X_train, y_train)
prediction_ada = ada.predict(X_test) # new output as prediction_ada, actual output as y_test
acc_ada = accuracy_score(y_true=y_test, y_pred= prediction_ada)*100
print("Overall accuracy of ADA model using test-set is : %f" %(acc_ada))

print("classification report for Random Forest")
print(classification_report(y_test,predictions_rf))
print("confusion matrix for Random Forest")
print(confusion_matrix(y_test,predictions_rf))
print("classification report for Adaboost")
print(classification_report(y_test,prediction_ada))
print("confusion matrix for Adaboost")
print(confusion_matrix(y_test,prediction_ada))

objects = ('Adaboost Classifier','Random Forest Classifier')

import matplotlib.pyplot as plt


y_pos = np.arange(len(objects))

performance = [acc_ada, acc_rf]
#performance = [91.42921754862053, 92.7860696517413, 93.08005427408412, 94.25599276345545, 95.52238805970149, 96.85662596110357, ]
plt.barh(y_pos, performance, align='center', alpha=1.0)
plt.yticks(y_pos, objects)
plt.xlabel('Model')
plt.xlabel('Accuracy')
plt.title('Accuracy per Model')

plt.show()
plt.savefig('accuracy_per_model.png')

import pickle

pickle.dump(rfc, open("rfmodel.pkl","wb"))

pickle.dump(ada, open("adamodel.pkl","wb"))
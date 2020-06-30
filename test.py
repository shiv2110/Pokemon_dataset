# Importing the libraries
import sys
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('pokemon_5.csv', index_col = 0)

# Creating matrix of features and target 
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Label Encoding the target
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# Splitting the dataset into train and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# One hot encoding the 1st column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')
x_train = np.array(ct.fit_transform(x_train))

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)

# Dealing with the imbalance
from imblearn.over_sampling import SMOTE 
sm = SMOTE(random_state = 2) 
x_train_res, y_train_res = sm.fit_sample(x_train, y_train.ravel()) 

# Training the model with Kernel SVM
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(x_train_res, y_train_res)

# Test set results
x_test = np.array(ct.transform(x_test))
x_test = sc.transform(x_test)
y_pred = classifier.predict(x_test)
#print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Test set result evaluation
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
#print(cm)
#print(accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report
#print(classification_report(y_test, y_pred))

# Single example prediction
'''
test_case = [[sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]]]
test_case = np.array(ct.transform(test_case))
test_case = sc.transform(test_case)
output = classifier.predict(test_case)

if output[0] == 1:
    print('Your pokemon is Legendary')
else:
    print('Your pokemon is not Legendary')
'''





# -*- coding: utf-8 -*-
"""Breast Cancer Analysis ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C6wM1Xh6L5iLnnSwYrg1teGbKqu0pfXu

#Importing Libs
"""

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

"""#Data collection & Processing"""

#Insert Data from sklern.
breast_cancer_dataset = sklearn.datasets.load_breast_cancer()

breast_cancer_dataset

#Insert data to a data frame
df = pd.DataFrame(breast_cancer_dataset.data, columns = breast_cancer_dataset.feature_names)

# print the the dataframe
df

#Cheack the Data Frame details
df.info()

# checking for missing values
df.isnull().sum()

#No null so no missing values

df.duplicated().sum()

#No duplicate data

df.head()

df.shape

# Adding 'target' column to data frame
df['label'] = breast_cancer_dataset.target

# Print last 5 rows of dataframe
df.tail()

df.shape

# statistical measures of the data
df.describe()

# checking the distribution of Target Varibale
df['label'].value_counts()

df.groupby('label').mean()

#Separating the for features and target

X = df.drop(columns='label', axis=1)
Y = df['label']
print(X)
print(Y)

#Splitting the data for training data & Testing data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

#Model Training
 #Logistic Regression

model = LogisticRegression()

# training model using Training data

model.fit(X_train, Y_train)

#Model Evaluation
  #Accuracy Score

# Training data accuracy
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
print('Training Accuracy= ', training_data_accuracy)

#Test data accuracy
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print('Test Accuracy = ', test_data_accuracy)

#Building a Predictive System

input_data = (19.69,21.25,130,1203,0.1096,0.1599,0.1974,0.1279,0.2069,0.05999,0.7456,0.7869,4.585,94.03,0.00615,0.04006,0.03832,0.02058,0.0225,0.004571,23.57,25.53,152.5,1709,0.1444,0.4245,0.4504,0.243,0.3613,0.08758)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one datapoint
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Breast cancer is Malignant')

else:
  print('The Breast Cancer is Benign')


# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer, StandardScaler, LabelEncoder
from sklearn.model_selection import StratifiedKFold, cross_val_score,GridSearchCV
from sklearn.linear_model import LogisticRegression
import pickle

train=pd.read_csv('loantrain.csv', index_col='Loan_ID')

mmodus = ['Gender','Married','Self_Employed','Dependents','Credit_History']
mmean = ['LoanAmount','ApplicantIncome','CoapplicantIncome','Loan_Amount_Term']

for feature in mmean:
        if feature in train.columns.values:
            train[feature] = train[feature].fillna(train[feature].mean())
            
for feature in mmodus:
        if feature in train.columns.values:
            train[feature] = train[feature].fillna(train[feature].value_counts().index[0])

categori = ['Gender','Married','Education','Self_Employed','Dependents',
            'Credit_History', 'Property_Area','Loan_Status']
for feature in categori:
        if feature in train.columns.values:
            train[feature] = LabelEncoder().fit_transform(train[feature])
x=train.drop('Loan_Status',axis=1)
y=train["Loan_Status"]
#print(x.shape)

regressor = LogisticRegression()

regressor.fit(x, y)

pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 1, 1,0,2,1000,2100,7000,360,
                      1,2]]))


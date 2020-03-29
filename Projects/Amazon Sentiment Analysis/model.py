# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

ind=["Review","Feedback","Naaa"]
data=pd.read_csv("Roman Urdu DataSet.csv",names=ind)
data.drop("Naaa",axis=1,inplace=True)

x=data["Review"]
y=data["Feedback"]
x.fillna(str(x.mode()),inplace=True)
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,
                            test_size=0,random_state=10)

text_clf=Pipeline([('vect',TfidfVectorizer()),
                   ('clf',MultinomialNB())])
text_clf.fit(xtrain,ytrain)



#regressor = LogisticRegression()

#regressor.fit(x, y)

pickle.dump(text_clf, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict(['Buzdilun se kya gilah pakistanyu']))


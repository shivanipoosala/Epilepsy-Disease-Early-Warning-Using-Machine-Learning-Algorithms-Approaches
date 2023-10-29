#importing libraries
import pandas as pd
import numpy as np
import pickle


df=pd.read_csv("Epilepsy_Dataset.csv")

#Feature Engineering
#Droping FirstName &LastName Column
df = df.drop(df.columns[[0, 1]],axis = 1)

#Renaming Attribute name
df=df.rename(columns={"Brain_tumor(stage)": "Brain_tumor"})

y=df.Affected.values   # values => np array
x=df.drop(["Affected"],axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)

# Randon Forest Classification
#Random Forest With Sklearn

from sklearn.ensemble import RandomForestClassifier
model= RandomForestClassifier(n_estimators=100,random_state=1) # n_estimators= number of trees
model.fit(x_train,y_train)

model_score = model.score(x_test,y_test)


print("random forest result: ", model.score(x_test,y_test))
pickle.dump(model,open('model.pkl','wb')) #we are Serializing our model by creating model.pkl and writing into it by 'wb'
model=pickle.load(open('model.pkl','rb')) #Deserializing - reading the file - "rb"
print("Sucess loaded")


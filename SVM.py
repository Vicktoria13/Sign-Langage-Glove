import pandas as pd
import sqlite3
from sklearn.svm import SVC
import joblib

#Algo de decisiontree

#Lecture la base de données
bdd= sqlite3.connect('gant.db')
curseur= bdd.cursor()

df= pd.read_sql_query("select * from Gangue ;",bdd)
# print(df)

#Séparation des valeurs
X=df.drop(columns=['signe','id'])
# X.drop(row=)
y=df['signe']

# print(X)
# print(y)

#Création du modèle
model = SVC()
model.fit(X,y)

# sauvegarde du modèle entraîné
joblib.dump(model,"SVM.joblib")

#lecture du modèle entraîné
# model = joblib.load("SVM.joblib")

# initialize data of lists.
data = {'d1100':[22],
        'd2100':[13],
        'd2200':[-6],
        'd3100':[4],
        'd3200':[1],
        'd4100':[124],
        'd4200':[89],
        'd5100':[63]}
 
# Create DataFrame
rec = pd.DataFrame(data)
# print(rec)

#test de prédictions
prediction = model.predict(rec)
print(prediction)


bdd.close()
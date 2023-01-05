import pandas as pd
import sqlite3
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

#Lecture la base de données
bdd= sqlite3.connect('gant.db')
curseur= bdd.cursor()

df= pd.read_sql_query("select * from Gangue ;",bdd)
print(df)

#Séparation des valeurs
X=df.drop(columns=['signe','id'])
y=df['signe']

#lecture du modèle entraîné
model = joblib.load("SVM.joblib")

#Séparation des données d'entraînement et de test
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.33)




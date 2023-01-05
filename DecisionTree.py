import pandas as pd
import sqlite3
from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

#Reconnaissance des signes avec l'algorithme des "Decision tree"
#Les attributs utilisés sont les valeurs d'angle de chaque capteur
#Les données sont stockées dans la base de données sqllite

#Lecture la base de données
bdd= sqlite3.connect('gant.db')
curseur= bdd.cursor()

#conversion en dataframe
df= pd.read_sql_query("select * from Gangue ;",bdd)

#Nettoyage de données
X=df.drop(columns=['signe','id'])
y=df['signe']

#Séparation des données d'entraînement et de test
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.33)

#Création du modèle
model = DecisionTreeClassifier()

#Entraînement des données
model.fit(x_train,y_train)

###Prédiction et MSE
Y=model.predict(x_test)

###test du modèle

#Avec K fold cross validation
Kf = KFold(n_splits=5)

res = cross_val_score(model,X,y, cv =Kf)

print(f"Précision moyenne = {res.mean()}")

# sauvegarde du modèle entraîné
joblib.dump(model,"Decisiontree.joblib")

#lecture du modèle entraîné
# model = joblib.load("Decisiontree.joblib")

# initialize data of lists.
# data = {'d1100':[22],
#         'd2100':[13],
#         'd2200':[-6],
#         'd3100':[4],
#         'd3200':[1],
#         'd4100':[124],
#         'd4200':[89],
#         'd5100':[63]}
 
# # Create DataFrame
# rec = pd.DataFrame(data)
# # print(rec)


# #test de prédictions
# prediction = model.predict(rec)
# print(prediction)


bdd.close()
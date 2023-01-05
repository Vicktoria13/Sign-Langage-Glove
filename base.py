import sqlite3
# import pandas as pd

bdd= sqlite3.connect('gant.db')
curseur= bdd.cursor()

#Création de la table Gangue
"""curseur.execute("CREATE TABLE Gangue(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,\
     signe TEXT,\
    d1100 INTEGER,\
    d2100 INTEGER,\
    d2200 INTEGER,\
    d3100 INTEGER,\
    d3200 INTEGER,\
    d4100 INTEGER,\
    d4200 INTEGER,\
    d5100 INTEGER)")
bdd.commit()"""

#Ajout de valeurs
"""curseur.execute("INSERT INTO Gangue(signe,\
    d1100,\
    d2100,\
    d2200,\
    d3100,\
    d3200,\
    d4100,\
    d4200,\
    d5100)\
    VALUES( ?,?,?,?,?,?,?,?,?)", ("Chiffre 2",0,0,0,90,90,90,90,90))
bdd.commit()"""

#Supprimer une donnée
sql="DELETE FROM Gangue WHERE id=8"
curseur.execute(sql)
bdd.commit()
curseur.close()

# bdd.close()
# #Récupération des données
# curseur.execute("select * FROM Gangue limit 2;")
# x=curseur.fetchall()
# print(x)

# df= pd.read_sql_query("select * from Gangue limit 2;",bdd)
# print(df)

bdd.close()
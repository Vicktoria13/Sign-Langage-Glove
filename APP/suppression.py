import sqlite3

#Ouverture de la base de données
bdd= sqlite3.connect('../gant.db')
curseur= bdd.cursor()

#Lecture du fichier temp
with open("temp.txt", "r+") as file: #introduction des variables
  id=file.readline() 
  file.close()

#Supprimer une donnée
sql="DELETE FROM Gangue WHERE id=" + id
curseur.execute(sql)
bdd.commit()
curseur.close()

print("élément supprimé")

bdd.close()


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



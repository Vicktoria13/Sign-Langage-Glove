import sqlite3

bdd= sqlite3.connect('../gant.db')
curseur= bdd.cursor()

#Lecture des valeurs saisies
with open("temp.txt", "r+") as file: #introduction des variables
  d1100=int(file.readline())
  d2100=int(file.readline())
  d2200=int(file.readline())
  d3100=int(file.readline())
  d3200=int(file.readline())
  d4100=int(file.readline())
  d4200=int(file.readline())
  d5100=int(file.readline())
  signe=file.readline() 
  file.close()

#Ajout de valeurs
curseur.execute("INSERT INTO Gangue(signe,\
    d1100,\
    d2100,\
    d2200,\
    d3100,\
    d3200,\
    d4100,\
    d4200,\
    d5100)\
    VALUES( ?,?,?,?,?,?,?,?,?)", (signe,d1100,d2100,d2200,d3100,d3200,d4100,d4200,d5100))
bdd.commit()


bdd.close()
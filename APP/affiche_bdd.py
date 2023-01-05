import sqlite3
import pandas as pd

bdd= sqlite3.connect('../gant.db')
curseur= bdd.cursor()

df= pd.read_sql_query("select * from Gangue ;",bdd)
print(df)

bdd.close()
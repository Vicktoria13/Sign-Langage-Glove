import serial
import time as tm
import sqlite3
#import pandas as pd

#Variable port série
ser = serial.Serial("COM3",9600,timeout=1)
print (ser)
#Attention à changer le port 
 
#Ouverture de la base de données
bdd= sqlite3.connect('gant.db')
curseur= bdd.cursor()

curseur.execute("select * FROM Gangue ")
x=curseur.fetchall()

#print(x)

def clean_data(data):
    """str ->str 
    Prends en paramètre une chaîne de caractère brute envoyée par le port série et renvoie la chaîne nettoyée"""

    #res:str
    res=''
    
    #parcours de la chaîne de caractères
    for i in data:
        if(i!='\\'  and i!='r' and i!='b' and i!='\'' and i!='n'):
            res= res + i
           
    return res
   
   
  
def recognize(ID,val,L):
    """int + int -> List[int]
    Prends en paramètre l'ID d'un capteur et met la val dans à sa bonne place dans la liste"""
    if(ID==1100):
        L[0]=val
        
    if(ID==2100):
        L[1]=val
        
    if(ID==2200):
        L[2]=val
        
    if(ID==3100):
        L[3]=val
        
    if(ID==3200):
        L[4]=val
        
    if(ID==4100):
        L[5]=val
        
    if(ID==4200):
        L[6]=val
        
    if(ID==5100):
        L[7]=val
        
    return L 


def abs(val):
    """Number -> Number
    Renvoie la valeur absolue de val"""
    
    if(val < 0):
        return -val
     
    return val
    

def affiche_val(L):
    """List[int]-> NULL
    Affiche les valeurs d'angle d'un tableau"""
    
    print("1100=",L[0]," 2100=",L[1]," 2200=",L[2]," 3100=",L[3],"\n3200=",L[4]," 4100=",L[5]," 4200=",L[6]," 5100=",L[7])


def verif_ecart(L1,L2,eps):
    """List[int] + List[int] -> int
    Vérifie si l'écart entre les valeurs absolues des valeurs des deux tableaux sont inférieures à eps.
    Renvoie 1 si c'est le cas, renvoie 0 sinon"""
    
    #l:int
    l=len(L1)
    
    #n1:int
    #n2:int
    
    for i in range(l):
        n1=abs(L1[i])
        n2=abs(L2[i])
        
        if(abs(n1-n2) > eps):
            return 0
            
    return 1
  

#List[int]
L=[-1,-1,-1,-1,-1,-1,-1,-1]

#List[int]
Ltemp=[-1,-1,-1,-1,-1,-1,-1,-1]

FIN=""
epsilon=20

indicateur=0


while 1:
    while (FIN!="OK"):

        if (indicateur==0):
            #Début de la mesure de temps
            start=tm.time()
            Ltemp=L
            indicateur=1

        #Lectures des données
        ID=str(ser.readline())
        angle=str(ser.readline())
        print(ID)
        print(angle)
        # Nettoyage des données
        if(ID!='' and len(ID)>1):
            ID_cleaned=int(clean_data(ID))
        if(angle!='' and len(angle)>1):
            angle_cleaned=int(clean_data(angle))
                
        # #Remplissage de L
        # recognize(ID_cleaned,angle_cleaned,L)

        # #Affichage des valeurs
        # affiche_val(L)
        # #affiche_val(Ltemp)

        # end=tm.time()
        # durée= end - start
        
        # if(durée >= 1.0):
        #     indicateur=0
        #     if(verif_ecart(L,Ltemp,epsilon)==1):
        #         FIN="OK"
              
        

    #Reconnaissance/Lire(Paula) du signe
    
    for i in x:
        if(i[2]-epsilon<L[0]<=i[2]+epsilon and i[3]-epsilon<L[1]<=i[3]+epsilon and i[4]-epsilon<L[2]<=i[4]+epsilon and i[5]-epsilon<L[3]<=i[5]+epsilon and i[6]-epsilon<L[4]<=i[6]+epsilon and i[7]-epsilon<L[5]<=i[7]+epsilon and i[8]-epsilon<L[6]<=i[8]+epsilon and i[9]-epsilon<L[7]<=i[9]+epsilon):
                print("Signe detecté :")
                print(i[1])
                tm.sleep(2)
    FIN=""

bdd.close()




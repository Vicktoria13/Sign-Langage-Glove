import serial
import time as tm
import sqlite3

#Ouverture de la base de données
bdd= sqlite3.connect('gant.db')
curseur= bdd.cursor()

#Variable port série
ser = serial.Serial("COM3",9600,timeout=1)


def clean_data(data):
    """str ->str 
    Prends en paramètre une chaîne de caractère brute envoyée par le port série et renvoie la chaîne nettoyée"""

    #res:str
    res=''
    
    #parcours de la chaîne de caractères
    for i in data:
        if(i!='\\'  and i!='r' and i!='b' and i!='\'' and i!='n' and i!=' '):
            res= res + i
    return res
   
   
  
def recognize(ID,val,L):
    """int + int -> List[int]
    Prends en paramètre l'ID d'un capteur et met val dans à sa bonne place dans la liste"""
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
L1=[-1,-1,-1,-1,-1,-1,-1,-1]

#List[int]
L2=[-1,-1,-1,-1,-1,-1,-1,-1]

p=1 

FIN=""
epsilon=5

calibrage=""
calibrage_int=-1


#Reception des données 
while (FIN!="OK"):

    while(calibrage_int!=9999):
        calibrage=clean_data(str(ser.readline()))
        
        if (calibrage!=''):
            calibrage_int=int(clean_data(calibrage))
            
    
    
    if(p%2!=0 and calibrage_int==9999 ):
        #Mesure 1
        for i in range(len(L1)):
            #Lectures des données
            ID=str(ser.readline())
            angle=str(ser.readline())
            # print(ID)
            # print(angle)
            #Nettoyage des données
            if(ID!=''):
                ID_cleaned=clean_data(ID)
                ID_cleaned=int(ID_cleaned)
            if(angle!=''):
                angle_cleaned=clean_data(angle)
                angle_cleaned=int(angle_cleaned)
            
            #Remplissage de L1
            recognize(ID_cleaned,angle_cleaned,L1)
            
        #Affichage des valeurs
        print("Liste 1")
        affiche_val(L1)   
    
    elif(p%2==0 and calibrage_int==9999):
        #Mesure 2
        for i in range(len(L2)):
            #Lectures des données
            ID=str(ser.readline())
            angle=str(ser.readline())
            #Nettoyage des données
            if(ID!=''):
                ID_cleaned=clean_data(ID)
                # print(ID_cleaned,"\n")
                ID_cleaned=int(ID_cleaned)
            if(angle!=''):
                angle_cleaned=clean_data(angle)
                angle_cleaned=int(angle_cleaned)
            
            #Remplissage de L2
            recognize(ID_cleaned,angle_cleaned,L2)
            
        #Affichage des valeurs
        print("Liste 2")
        affiche_val(L2)

    p=p+1
    calibrage_int=-1
    tm.sleep(2)
    if(verif_ecart(L1,L2,epsilon)):
        print("Validation des données\nPour valider les données saisir OK")
        print("Votre saisie: ")
        FIN=input()
    
   
#Saisie du nom du signe
print("Veuillez saisir le nom d'un signe")
print("Votre saisie: ")
Signe=input()
 
#Ajout de valeurs dans la base données
curseur.execute("INSERT INTO Gangue(signe,\
    d1100,\
    d2100,\
    d2200,\
    d3100,\
    d3200,\
    d4100,\
    d4200,\
    d5100)\
    VALUES( ?,?,?,?,?,?,?,?,?)", (Signe,L1[0],L1[1],L1[2],L1[3],L1[4],L1[5],L1[6],L1[7]))
    
    
print("Confirmation finale : pour confirmer saisir OK")
confirm=input()

if(confirm=="OK"):
    bdd.commit()
    
#ajout des valeurs dans la base de données
#synchronisation de l'arduino et du code python
#rajouter Serial.print Pivot pour la synchronisation du type 9999    
#Rajouter 
    
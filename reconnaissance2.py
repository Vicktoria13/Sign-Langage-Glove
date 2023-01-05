from cgi import print_environ_usage
import serial
import time as tm
import sqlite3
import pandas as pd
import sklearn
import joblib
import pygame as py

###----------------------------------------------------------------------------------
###Affichage graphique

#initialisation
py.init()

#RGBdu blanc
white=(255,255,255)
green = (0, 255, 0)
black = (0, 0, 0)
red = (255,0,0)

#Taille de la fenêtre
X=720
Y=480

#Création de la fenêtre
display_surface = py.display.set_mode((X,Y))

py.display.set_caption("Gan'gue des signes")

font = py.font.Font('freesansbold.ttf', 32)

text = font.render("Test",True,black)
textRect = text.get_rect()
textRect.center = (X//2,Y//2)

def trouve_image(signe):
    path = "./images/" + signe[0] +".png"
    return path

def Recherche():
    text = font.render("Recherche",True,black)
    textRect = text.get_rect()
    textRect.center = (X//2,20)
    display_surface.blit(text,textRect)

def affiche_text(text,x,y,color):
    text = font.render(text,True,color)
    textRect = text.get_rect()
    textRect.center = (x,y)
    display_surface.blit(text,textRect)

def signe_trouve(signe):
    affiche_text(f"signe trouvé : {signe[0]}",X//2,Y//2-50,black)

def affiche_ID():
    L=[1100,2100,2200,3100,3200,4100,4200,5100]
    for i in range(len(L)):
        affiche_text(str(L[i]),40 + i*90,70,red)

def affiche_valeur(L):
    for i in range(len(L)):
        affiche_text(str(L[i]),40 + i*90,100,black)

def affiche_signe(signe):
    path = trouve_image(signe)
    image = py.image.load(path)
    display_surface.blit(image,(X//2-152,Y//2-30))
    
###----------------------------------------------------------------------------------

# def affiche_valeur(signe):
#Variable port série
ser = serial.Serial("COM3",9600,timeout=1)
# print (ser)
#Attention à changer le port 
 
#Ouverture de la base de données
bdd= sqlite3.connect('gant.db')
curseur= bdd.cursor()

curseur.execute("select * FROM Gangue ")
x=curseur.fetchall()

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
            
    return True
  

#List[int]
L=[-1,-1,-1,-1,-1,-1,-1,-1]

#List[int]
Ltemp=[-1,-1,-1,-1,-1,-1,-1,-1]

FIN=""
epsilon=5

indicateur=0


while 1:
    while (FIN!="OK"):
        #Affichage
        display_surface.fill(white)
        Recherche()
        affiche_ID()

        if (indicateur==0):
            #Début de la mesure de temps
            start=tm.time()
            Ltemp=L
            indicateur=1

        #Lectures des données
        ID=str(ser.readline())
        angle=str(ser.readline())

        #Nettoyage des données
        if(ID!=''):
            ID_cleaned=int(clean_data(ID))
        if(angle!=''):
            angle_cleaned=int(clean_data(angle))
                
        #Remplissage de L
        recognize(ID_cleaned,angle_cleaned,L)

        #Affichage des valeurs
        # affiche_val(L)
        affiche_valeur(L)
        py.display.update()
        #tm.sleep(3)
        #affiche_val(Ltemp)

        end=tm.time()
        durée= end - start
    
        if(durée >= 2.0):
            indicateur=0
            
            if(verif_ecart(L,Ltemp,epsilon)):
                FIN="OK"
        
        for event in py.event.get() :
            if event.type == py.QUIT :
                py.quit()
                quit()

            py.display.update()
              
    #Reconnaissance/Lire(Paula) du signe
    # initialize data of lists.
    data = {'d1100':[L[0]],
            'd2100':[L[1]],
            'd2200':[L[2]],
            'd3100':[L[3]],
            'd3200':[L[4]],
            'd4100':[L[5]],
            'd4200':[L[6]],
            'd5100':[L[7]]}
    
    # Create DataFrame
    rec = pd.DataFrame(data)

    #lecture du modèle entraîné
    model = joblib.load("DecisionTree.joblib")
    # model = joblib.load("SVM.joblib")

    #test de prédictions
    prediction = model.predict(rec)
    print(prediction)
    FIN=''
    signe_trouve(prediction)
    affiche_signe(prediction)
    py.display.update()

    for event in py.event.get() :
        if event.type == py.QUIT :
            py.quit()
            quit()

        py.display.update()
    tm.sleep(2)
    
bdd.close()




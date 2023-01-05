#from curses import window
import tkinter as tk
from tkinter.messagebox import YES
from turtle import width
import time as tm

from pyrsistent import v




### Définitions des fonctions
def affiche():
    exec(open("affiche_bdd.py").read(), globals())

def suppression():
    id = id_entry.get()
    with open("temp.txt", "w+") as file:
        file.write(id)
    exec(open("suppression.py").read(), globals())

def ajout_auto():
    serial = serial_entry.get()
    with open("temp.txt", "w+") as file:
        file.write(serial)
    exec(open("ajout_auto.py").read(), globals())

def reconnaissance():
    serial = serial_entry.get()
    with open("temp.txt", "w+") as file:
        file.write(serial)
    exec(open("reconnaissance.py").read(), globals())

def ajout_manuel():
    vsigne = signe_entry.get()
    vd1100 = d1100_entry.get()
    vd2100 = d2100_entry.get()
    vd2200 = d2200_entry.get()
    vd3100 = d3100_entry.get()
    vd3200 = d3200_entry.get()
    vd4100 = d4100_entry.get()
    vd4200 = d4200_entry.get()
    vd5100 = d5100_entry.get()
    with open("temp.txt", "w+") as file:
        file.write(vd1100 + "\n")
        file.write(vd2100 + "\n")
        file.write(vd2200 + "\n")
        file.write(vd3100 + "\n")
        file.write(vd3200 + "\n")
        file.write(vd4100 + "\n")
        file.write(vd4200 + "\n")
        file.write(vd5100 + "\n")
        file.write(vsigne )
    exec(open("ajout_manuel.py").read(), globals())
    

#Création de la fenêtre
window=tk.Tk()

#paramètres de la fenêtre
window.title("Gan'gue des signes")
window.geometry("700x600")
window.configure(background="white")

# window.config(background='black')

# #Ajout du background
# background_image=tk.PhotoImage(file ="background.png")
# background_label = tk.Label(window, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Ajout du logo
logo = tk.PhotoImage(file = "logo.png")
canvas = tk.Canvas(window,width=300, height=300,bg="white")
canvas.create_image(0,0,anchor=tk.NW, image=logo)
canvas.pack()

#Ajout de la première frame
# bd=1, relief=tk.SUNKEN
frame1 = tk.Frame(window,bg="white")
frame1.pack(side=tk.LEFT,ipadx=20)

#Ajout de la deuxième frame
frame2 = tk.Frame(window,bg="white")
frame2.pack(side=tk.RIGHT,ipadx=30)

#éléments de la frame de gauche
BDD = tk.Label(frame1, text="Options sur la BDD",font=("Arial",20),bg="yellow")
BDD.pack(pady=10)

bouton_affichage = tk.Button(frame1,text="Afficher la base de données",font=("Arial",12),command = affiche)
bouton_affichage.pack(pady=5)

bouton_ajout_auto = tk.Button(frame1,text="Ajouter automatiquement \n un élément à la base de données",font=("Arial",12),command= ajout_auto)
bouton_ajout_auto.pack(pady=5)

bouton_ajout_manuel = tk.Button(frame1,text="Ajouter manuellement \n un élément à la base de données",font=("Arial",12),command=ajout_manuel)
bouton_ajout_manuel.pack(pady=5)

bouton_suppression = tk.Button(frame1,text="Supprimer un élément \n de la base de données",font=("Arial",12),command = suppression)
bouton_suppression.pack(pady=5)

#éléments de la frame de droite
gant = tk.Label(frame2, text="Options avec le gant",font=("Arial",20),bg="yellow")
gant.pack()

bouton_reconnaissance = tk.Button(frame2,text="Utiliser la reconnaissance de signes",font=("Arial",12),command= reconnaissance)
bouton_reconnaissance.pack(pady=10)

id = tk.Label(frame2, text = "Id de l'élément à supprimer", font=("Arial", 12), bg='white', fg='black')
id.pack()
id_entry = tk.Entry(frame2, text = "id", font=("Arial", 12), bg='grey', fg='black')
id_entry.pack()

serial = tk.Label(frame2, text = "Port série à utiliser", font=("Arial", 12), bg='white', fg='black')
serial.pack()
serial_entry = tk.Entry(frame2, text = "serial", font=("Arial", 12), bg='grey', fg='black')
serial_entry.insert(tk.END, 'COM14')
serial_entry.pack()

#Création d'une deuxième fenêtre
window2=tk.Toplevel(window)

#Paramètres de la deuxième fenêtre
window2.title("Paramètres ajout manuel")
window2.geometry("450x400")
window2.configure(background="white")

#Nom du signe
signe = tk.Label(window2, text = "Nom du signe", font=("Arial", 12), bg='white', fg='black')
signe.pack()
signe_entry = tk.Entry(window2, text = "signe", font=("Arial", 12), bg='grey', fg='black')
signe_entry.insert(0,'signe')
signe_entry.pack()

#Création des frames
frame3 = tk.Frame(window2,bg="white",relief=tk.SUNKEN )
frame3.pack(side=tk.LEFT,ipadx=20)
frame4 = tk.Frame(window2,bg="white")
frame4.pack(side=tk.RIGHT,ipadx=30)

#Ajout des valeurs d'angles dans la première frame
#d1100
d1100 = tk.Label(frame3, text = "Valeur d1100", font=("Arial", 12), bg='white', fg='black')
d1100.pack()
d1100_entry = tk.Entry(frame3, text = "d1100", font=("Arial", 12), bg='grey', fg='black')
d1100_entry.insert(0,0)
d1100_entry.pack()

#d2100
d2100 = tk.Label(frame3, text = "Valeur d2100", font=("Arial", 12), bg='white', fg='black')
d2100.pack()
d2100_entry = tk.Entry(frame3, text = "d2100", font=("Arial", 12), bg='grey', fg='black')
d2100_entry.insert(0,0)
d2100_entry.pack()

#d2200
d2200 = tk.Label(frame3, text = "Valeur d2200", font=("Arial", 12), bg='white', fg='black')
d2200.pack()
d2200_entry = tk.Entry(frame3, text = "d2200", font=("Arial", 12), bg='grey', fg='black')
d2200_entry.insert(0,0)
d2200_entry.pack()

#d3100
d3100 = tk.Label(frame3, text = "Valeur d3100", font=("Arial", 12), bg='white', fg='black')
d3100.pack()
d3100_entry = tk.Entry(frame3, text = "d3100", font=("Arial", 12), bg='grey', fg='black')
d3100_entry.insert(0,0)
d3100_entry.pack()

#Ajout de valeurs d'angle dans la deuxième frame
#d3200
d3200 = tk.Label(frame4, text = "Valeur d3200", font=("Arial", 12), bg='white', fg='black')
d3200.pack()
d3200_entry = tk.Entry(frame4, text = "d3200", font=("Arial", 12), bg='grey', fg='black')
d3200_entry.insert(0,0)
d3200_entry.pack()

#d4100
d4100 = tk.Label(frame4, text = "Valeur d4100", font=("Arial", 12), bg='white', fg='black')
d4100.pack()
d4100_entry = tk.Entry(frame4, text = "d4100", font=("Arial", 12), bg='grey', fg='black')
d4100_entry.insert(0,0)
d4100_entry.pack()

#d42
d4200 = tk.Label(frame4, text = "Valeur d4200", font=("Arial", 12), bg='white', fg='black')
d4200.pack()
d4200_entry = tk.Entry(frame4, text = "d4200", font=("Arial", 12), bg='grey', fg='black')
d4200_entry.insert(0,0)
d4200_entry.pack()

#d5100
d5100 = tk.Label(frame4, text = "Valeur d5100", font=("Arial", 12), bg='white', fg='black')
d5100.pack()
d5100_entry = tk.Entry(frame4, text = "d5100", font=("Arial", 12), bg='grey', fg='black')
d5100_entry.insert(0,0)
d5100_entry.pack()
d1=d1100_entry.get()
d2=d2100_entry.get()


#affichage de la fenêtre
window.mainloop()
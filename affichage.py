import pygame as py

#initialisation
py.init()

#RGBdu blanc
white=(255,255,255)
green = (0, 255, 0)
black = (0, 0, 0)

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
    path = "./images/" + signe +".png"
    return path

def Recherche():
    text = font.render("Recherche",True,black)
    textRect = text.get_rect()
    textRect.center = (X//2,20)
    display_surface.blit(text,textRect)

def signe_trouve(signe):
    text = font.render(signe,True,black)
    textRect = text.get_rect()
    textRect.center = (X//2,20)
    display_surface.blit(text,textRect)


path = trouve_image("chiffre_1")
image = py.image.load(path)

while True:
    display_surface.fill(white)
    # Recherche()
    signe_trouve("chiffre_1")
    display_surface.blit(image,(X//2,Y//2))
    for event in py.event.get() :
        if event.type == py.QUIT :
            py.quit()
            quit()

        py.display.update()


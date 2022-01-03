# header
"""
auteur : Thibaut Weber
13/12/2021
Projet Space Invaders
"""

# A FAIRE : fonctions right, left pour déplacer le vaisseau

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time
import random


# création de la fenêtre graphique
Mafenetre = Tk()
Mafenetre.title('Space Invaders')

# on définit le canevas (zone graphique)
canevas = Canvas(Mafenetre, width=640, height=480, bg='black')

# on définit les touches qui vont permettre au joueur de déplacer le vaisseau
canevas.bind("<Right>", right)
canevas.bind("<Left>", left)
canevas.bind("<space>", tir)
canevas.bind("<p>", pause)   #definir les 4 fonctions right, left, tir et pause

canevas.grid(row=1,column=0,columnspan=2,rowspan=3) # a pour effet de placer canevas dans une zone avec les numéros de lignes 1-3 et les numéros de colonnes 0-1

# on ajoute une image de fond
photo = PhotoImage(file='earth.gif')
canevas.create_image(320,240,image=photo)

#on crée les boutons pour lancer une partie et pour quitter le jeu
Button(Mafenetre, text="Nouvelle partie", command=nouvelle_partie).grid(row=2,column=2,sticky=N,padx=5) #creerla foncrion nouvelle partie
Button(Mafenetre, text="Quitter", command=Mafenetre.destroy).grid(row=3,column=2,sticky=N,padx=5)

#on crée les fonctions qui permettent au vaisseau de se déplacer

def left():
    global 
    
def right():
    global
    

#on définit le vaisseau

vaisseau=[]
xv1=0
yv1=0
xv2=0
yv2=0

#on définit les aliens 

alien1=[]
alien2=[]
alien3=[]

ListeAliens=[alien1, alien2, alien3]
aliens=[]

#on définit les listes qui contiennent les coordonnées des aliens

CoordAlien1=[]
CoordAlien2=[]
CoordAlien3=[]

ListeCoordAliens=[CoordAlien1, CoordAlien2, CoordAlien3]

NbAlien1 = 6
NbAlien2 = 6
NbAlien3 = 6

NbAliens = [NbAlien1, NbAlien2, NbAlien3]

#on définit les positions initiales des aliens

xe1, ye1 = 0,0
xe2, ye2 = 0,0
xe3, ye3 = 0,0

#on crée les aliens

def Alien1():
    global NbAliens, ListeCoordAliens, xe1, ye1
    ListeCoordAliens[0].append([xe1, ye1])
    aliens=[]
    aliens.append(canevas.create_rectangle(xe1, ye1, xe1+60, ye1+20, fill="blue")) #le haut de l'alien 1
    aliens.append(canevas.create_rectangle(xe1, ye1, xe1+20, ye1+40, fill="blue")) #le bloc en bas à gauche de l'alien 1
    aliens.append(canevas.create_rectangle(xe1+40, ye1, xe1+60, ye1+60, fill="blue")) #le bloc en bas à droite de l'alien 1
    NbAliens[0].append(aliens)
    xe1+=80 #on espace les aliens1 de 4 carrés

def Alien2():
    global NbAliens, ListeCoordAliens, xe2, ye2
    ListeCoordAliens[1].append([xe2, ye2])
    aliens=[]
    aliens.append(canevas.create_rectangle(xe2, ye2, xe2+20, ye2+40, fill="violet")) #la gauche l'alien 2
    aliens.append(canevas.create_rectangle(xe2+40, ye2, xe2+60, ye2+40, fill="violet")) #la droite de l'alien 2
    aliens.append(canevas.create_rectangle(xe2+20, ye2+20, xe2+40, ye2+60, fill="violet")) #le centre de l'alien 2
    NbAliens[1].append(aliens)
    xe2+=80 #on espace les aliens2 de 4 carrés
    
def Alien3():
    global NbAliens, ListeCoordAliens, xe2, ye2
    ListeCoordAliens[2].append([xe2, ye2])
    aliens=[]
    aliens.append(canevas.create_rectangle(xe3+20, ye3, xe3+40, ye3+60, fill="red")) #l'axe vertical de l'alien 3
    aliens.append(canevas.create_rectangle(xe3, ye3+20, xe3+60, ye3+40, fill="red")) #l'axe horizontal de l'alien 3
    NbAliens[2].append(aliens)
    xe3+=80 #on espace les aliens3 de 4 carrés
    
    
# on positionne les aliens sur le canvas

i=0

while i<6:
    Alien1()
    Alien2()
    Alien3()
    i+=1              

#création du widget "Bonjour le monde"
labelHello = Label (Mafenetre,text = "Hello world", fg='blue')

# positionnement du widget
labelHello.pack()

# création du widget bouton
buttonQuitt = Button (Mafenetre, text="QUITTER", fg = 'red', command = Mafenetre.destroy)

# positionnement du widget
buttonQuitt.pack()

# lancement du gestionnaire d'évènements
Mafenetre.mainloop()

  
# cette fonction réinitialise le jeu selon la volonté du joueur
  
def new_game():
    global xe, ye, xe2, ye2, xe3, ye3
    
    DebutJeu=1
    
    #on utilise l'image du jeu
    
    photo = PhotoImage(file='earth.gif')
    can.create_image(320,240,image=photo)
    
    
    
    

                                           




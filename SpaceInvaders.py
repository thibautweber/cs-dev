# header
"""
auteur : Thibaut Weber
13/12/2021
Projet Space Invaders
"""

from tkinter import Tk, Button, Canvas, Label, StringVar, Entry
import time
import random

# création de la fenêtre graphique
mw = Tk()

#création du widget "Bonjour le monde"
labelHello = Label (mw,text = "Hello world", fg='blue')

# positionnement du widget
labelHello.pack()

# création du widget bouton
buttonQuitt = Button (mw, text="QUITTER", fg = 'red', command = mw.destroy)

# positionnement du widget
buttonQuitt.pack()

# lancement du gestionnaire d'évènements
mw.mainloop()





from Space_invaders import *

class Alien:
    
    Compteur=0
    def __init__(self):
        Alien.Compteur += 1
        self.Compteur=Alien.Compteur
        self.vivant=True
        self.x=self.Compteur*(ecart_alien+largeur_alien)
        Alien.y=hauteur_alien_ligne1
        Alien.dir=1
        Alien.vitesse=VitesseAlien
    
    def Creation(self):
        #self.apparence=canevas.create_rectangle(self.x-largeur_alien/2,Alien.y-hauteur_alien/2,self.x+largeur_alien/2,Alien.y+hauteur_alien/2,width=2,outline='white')
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=ImageAlien)

    def Affichage(self):
        #canevas.coords(self.apparence , self.x-largeur_alien/2 ,Alien.y-hauteur_alien/2 , self.x+largeur_alien/2 ,Alien.y+hauteur_alien/2)
        canevas.coords(self.apparence,self.x,self.y)
    

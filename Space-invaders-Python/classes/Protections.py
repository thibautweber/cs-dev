from Space_invaders import *

class Protections:
    Compteur=0
    def __init__(self):
        Protections.Compteur+=1
        self.Compteur=Protections.Compteur
        self.x=largeur*self.Compteur/(nbre_protections+1)
        Protections.y=posY_protections
        self.Resistance=resistance_protections
        self.Apparence=canevas.create_rectangle(self.x,self.y,self.x+largeur_protections,self.y+hauteur_protections,width=2,outline='purple',fill='white')
        self.VieProtection=canevas.create_text(self.x+largeur_protections/2,self.y+hauteur_protections/2,text=str(self.Resistance),fill='red')
        
    def Update(self):
        self.Resistance-=1
        if self.Resistance>0:
            canevas.itemconfig(self.VieProtection,text=(str(self.Resistance)))
        else:
            self.Destruction()
    
    def Destruction(self):
        canevas.delete(self.Apparence)
        canevas.delete(self.VieProtection)
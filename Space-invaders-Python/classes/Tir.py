from Space_invaders import *

class Tir:
    
    Compteur=0
    def __init__(self):
        self.x=vaisseau.x
        self.y=vaisseau.y
        self.apparence=canevas.create_line(self.x , self.y-4 , self.x ,\
        self.y , fill='white')
        self.encours=True
        Tir.Compteur+=1
    
    def Affichage(self):
        canevas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
    
    def Deplacement(self):
        if self.encours:
            self.y-=VitesseTir
            self.Affichage()
            self.FinTir()
            mw.after(5,self.Deplacement)
      

    def FinTir(self):
        if self.y<0:
            self.encours=False
            canevas.delete(self.apparence)
            del Tirs[0]
            Tir.Compteur-=1
        else:
            for i in ennemie:
                if i.vivant and self.y>=i.y and self.y<=i.y+hauteur_alien and self.x<=i.x+largeur_alien and self.x>=i.x:
                    self.Destruction()
                    canevas.delete(i.apparence)
                    i.vivant=False
                    Alien.vitesse+=AccelerationAlien
                    Points(PointsAlien)
                    PartieGagnee()


    def Destruction(self):
        self.encours=False
        canevas.delete(self.apparence)
        del Tirs[0]
        Tir.Compteur-=1
                    
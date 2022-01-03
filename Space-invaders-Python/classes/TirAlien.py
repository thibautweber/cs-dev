from Space_invaders import *

class TirAlien:
    
    def __init__(self,i):
        self.x=ennemie[i].x
        self.y=ennemie[i].y
        self.apparence=canevas.create_line(self.x , self.y-4 , self.x ,\
        self.y , fill='white')
        self.encours=True
        self.Deplacement()

    def affichage(self):
        canevas.coords(self.apparence , self.x , self.y-4 , self.x , self.y)
        
    def Deplacement(self):
        if self.encours:
            self.y+=VitesseTir
            self.affichage()
            self.FinTir()
            mw.after(5,self.Deplacement)
    
    def FinTir(self):
        global Vies
        if self.y>hauteur:
            self.encours=False
            canevas.delete(self.apparence)
            del TirsAlien[0]
        elif self.y>=vaisseau.y-5 and self.y<=vaisseau.y+5 and\
            self.x<=vaisseau.x+largeur_vaisseau/2 and\
            self.x>=vaisseau.x-largeur_vaisseau/2 :
                self.encours=False
                canevas.delete(self.apparence)
                del TirsAlien[0]
                Vies-=1
                vaisseau.ViePerdue()
                AffichageVies(Vies)
                if Vies==0:
                    PartiePerdue()
        else:
            for i in Defences:
                if i.Resistance>0 and self.x>=i.x and self.x<=i.x+largeur_protections and self.y>=Protections.y and self.y<=Protections.y+hauteur_protections:
                    i.Update()
                    self.encours=False
                    canevas.delete(self.apparence)
                    del TirsAlien[0]
        
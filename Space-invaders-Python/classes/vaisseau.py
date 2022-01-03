from Space_invaders import *

class vaisseau:
    
    def __init__(self):
        '''self.apparence=canevas.create_oval(posX-largeur_vaisseau/2,\
        posY-hauteur_vaisseau/2,posX+largeur_vaisseau/2,\
        posY+hauteur_vaisseau/2,width=2,outline='white')'''

        self.x=posX
        self.y=posY
        self.apparence=canevas.create_image(self.x,self.y,anchor='center',image=ImageVaisseau)


    def deplacement(self,dir):
        if self.x>=largeur_vaisseau and dir==-1:
            self.x+=VitesseDeplacement*dir
        elif self.x<=largeur-largeur_vaisseau and dir==1:
            self.x+=VitesseDeplacement*dir
        self.Affichage()
        
    def Affichage(self):
        canevas.coords(self.apparence,self.x,self.y)
        
        
    def ViePerdue(self):
        canevas.itemconfig(self.apparence,image=ImageDestroy)
        mw.after(500,self.RetourApparenceNormale)
        
    def RetourApparenceNormale(self):
        canevas.itemconfig(self.apparence,image=ImageVaisseau)
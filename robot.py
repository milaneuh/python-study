class Robot:
    def __init__(self,taille,couleur,poid):
        self.taille = taille
        self.couleur = couleur
        self.poid = poid

    def introduce(self):
        print("Bonjour moi c'est {} je suis {} et je fais {}".format(self.taille,self.couleur,self.poid))


    def changerPoid(self):
        
        nouveauPoid =int(intput("Veuillez indiquez le nouveau poid du modèle {}"))

        nouveauPoid
        
        self.poid = nouveauPoid

        print(self.poid)
class Vehicule:
    """Classe représentant un véhicule"""
    def __init__(self, modele,marque):

        self.modele = modele
        self.marque = marque
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaine"""
        return "{0} {1}".format(self.marque, self.modele)

class Voiture(Vehicule):
    """Classe définissant une voiture.
    Elle hérite de la classe Véhicule"""

    def __init__(self, modele, marque , kmtrage):
        """Une voiture  se définit par son kilométrage et son modele"""

        Vehicule.__init__(self, modele)
        Vehicule.__init__(self, marque)
        self.kmtrage = kmtrage
    
    def __str__(self):

        return "{0} {1}, Kilométrage : {3} km".format(self.marque, self.modele, self.kmtrage)
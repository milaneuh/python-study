import os

class Personne: # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self, nom, prenom): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.nom = nom


        self.prenom = prenom

        self._age = 33

        self._lieu_de_residence = "Paris"


    def _get_age(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture à 
        l'attribut 'age'"""

        print("{} , Voici ton âge.".format(self.prenom))

        return self._age

    def _set_age(self, nouveau_age):
        """Méthode appelée quand on souhaite modifier l'âge"""
       
        print("Il semble que {} ai grandi".format( self._age))

        self._age = nouveau_age

    def _del_age(self):
        """Méthode appelée quand on souhaite supprimer l'âge"""
        print("Nous allons supprimer l'âge")
        del  self.age


    age = property(_get_age, _set_age,_del_age)



    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieu_residence'"""
        
        
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)
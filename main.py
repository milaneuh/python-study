class ZDict:
    """Classe enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}
    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        if index in self._dictionnaire:
            return self._dictionnaire[index]

        else:
            raise AttributeError("Cet item n'existe pas dans le dictionnaire")
    
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        
        self._dictionnaire[index] = valeur
    
    def __delitem__(self, index):
        """Cette méthode est appelée quand on veut supprimer un item d'un conteneur"""

        del self._dictionnaire[index]
        print("L'item a été supprimé")


    def __len__():
        """Cette méthode est appelée quand on veut savoir la taille de l'objet"""

        return len(self._dictionnaire)
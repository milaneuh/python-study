"""Le but du TP est de créer un dictionnaire ordonné composé de deux listes"""

class DictionnaireOrdonne: #Définition de notre classe dictionnaire
    """Classe Dictionnaire qui va se composer de 
    -une liste de clefs
    -une liste de valeurs"""
    def __init__(self): #Notre méthode constructeur 
        print("Nous allons mettre en place votre dictionnaire.")
        List.__init__(self)

    
    
    def __repr__(self): #Notre méthode de représentation de l'objet
        print("Voici votre dictionnaire : /n")
        scan = 0 #Pointeur qui va nous permettre de naviguer dans nos deux listes 
        longueur_list = len(self._ClefList)
        while scan != longueur_list:
            print('/n')
            print("DictonnaireOrdonne[{1}] : {2}".format(self._ClefList[scan], self._ValList[scan]))
            scan +=1 #On rajoute 1 au pointeur du print
    
    
    def __str__(self):
        print("Voici votre dictionnaire : ")
        scan = 0 #Pointeur qui va nous permettre de naviguer dans nos deux listes 
        longueur_list = len(self._ClefList)
        
        if len(self._ClefList) <+ 0:
            print("{}")
        else:
            while scan != longueur_list:
                print('/n')
                print("DictonnaireOrdonne[{1}] : {2}".format(self._ClefList[scan], self._ValList[scan]))
                scan +=1 #On rajoute 1 au pointeur du print        
   
   
   
    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._ValList[index]"""
        
        return self._ValList[index]
   
   
   
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._ClefList[index],self._ValList[index] """
        if index in self._ClefList == True or (index - 1) in self._ClefList == True or index == 0:#On vérifie que l'index existe ou que il y a une clef avant cette index pour ne pas avoir de trou dans la liste    
            self._ClefList[index] = index #On incrémente l'index comme clef pour la valeurs de la liste val
            self._ValList[index] = valeur #On incrémente la valeurs dans la liste Val
        else:
            raise IndexError
    
    def __contains__(self, objet):
        pass




class List(DictionnaireOrdonne):

    """Classe définissant la liste des clefs  et des valeurs du dictionnaire ordonnées"""
    
    
    """On ajoute une variable pointeur qui va nous permettre d'ajouter les clefs de la liste 1 au même emplacement que les valeurs associées dans la liste 2"""
    pointeur = 0 #Le compteur vaut 0 au départ
    
    def __init__(self):
        """Par défaut nos listes sont vides"""
        self._ClefList = []

        self._ValList = []

    def _get_list(self):
        pass
    def _set_list(self, clef_a_ajouter, valeur_a_ajouter):
        """Méthode permettant de ajouter une clefs  et une valeur à notre liste et donc à notre dictionnaire"""

        self._ClefList[pointeur] = clef_a_ajouter
        self._ValList[pointeur] = valeur_a_ajouter
        pointeur += 1 #On rajoute 1 au pointeur 
   
    # On va dire à python que notre attribut dico pointe vers une
    # propriété 
    dico = property(_get_list, _set_list)

class Checker(List):
    """Classe qui va vériffier que il n'y ai pas d'erreur dans nos listes"""
    def __init__(self):
        List.__init__(self)
    def __getattribute__(self, _ClefList):
        """Si pythone ne trouve pas la Clef demandée, il appelle cette méthode et affiche une alerte"""
        print("Cette clef n'existe pas dans votre dictionnaire.")

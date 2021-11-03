"""Le but du TP est de créer un dictionnaire ordonné composé de deux listes"""
from operator import attrgetter

class DictionnaireOrdonne: #Définition de notre classe dictionnaire
    """Classe Dictionnaire qui va se composer de 
    -une liste de clefs
    -une liste de valeurs"""

    
    def __init__(self, base = {}, **donnes):#Notre méthode constructeur
        print("\nData type of argument :",type(donnes))

        """Introduction d'une Loop pour transformer nos données en dictionnaire"""
        
        for key, value in donnes.items():
            base[key] = value
        
        self.keyList = list(base) #On transforme nos cléfs en liste
        
        self.valList = list(base.values()) #On transforme nos valeurs en liste 

        self._dictionnaire = base
            
    def __repr__(self): 
        
        """Méthode qui va nous servir d'afficher le dictionnaire lorsqu'on écrit notre object dans le pannel de commande"""
        
        base = {} #Dictionnaire qui va nous servir d'affichage
        
        for key in self.keyList: #Introduction d'une loop pour transformer nos 2 listes en dictionnaire Key/Val
            for value in self.valList:
                base[key] = value
                self.valList.remove(value)
                break
        return "Votre Dictionnaire : \n {}".format(base) #On affiche le dictionnaire.
            
    def __str__(self): 
        
        """Méthode qui va nous servir d'afficher le dictionnaire lorsqu'on écrit notre object dans le pannel de commande"""
        
        base = {} #Dictionnaire qui va nous servir d'affichage
        
        for key in self.keyList: #Introduction d'une loop pour transformer nos 2 listes en dictionnaire Key/Val
            for value in self.valList:
                base[key] = value
                self.valList.remove(value)
                break
        return "Votre Dictionnaire : \n {}".format(base) #On affiche le dictionnaire.

    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        print(self._dictionnaire[index])          
    
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        
        self._dictionnaire[index] = valeur #On montre le dictionnaire
        if self.keyList.__contains__(index): #On vérifie que on ne fait pas de doublons
            pos = self.keyList.index(index) #On met un pointeur sur la valeur à écraser
            self.valList[pos] = valeur #On écrase la valeur
        else:
            #Si il n'y a pas de doublons on ajouter simplement la clef et la valeur 
            self.keyList.append(index) 
            self.valList.append(valeur)
    
    def __contains__(self,param1):
        """Cette méthode est appelée quand on veut savoir si une clef existe dans notre dictionnaire"""
        return True if param1 in self.keyList else False #On utilise in booléen et l'opérateur "in" pour cette méthode

    def __delitem__(self, index):
        """Cette méthode est appelée quand on veut supprimer un item du dictionnaire"""
        pos3 = self.keyList.index(index) #On récupère l'emplacement de l'item dans les 2 listes
        del self._dictionnaire[index] #On le supprime dans le dictionnaire
        del self.keyList[pos3] #On supprime sa clef
        del self.valList[pos3] #On supprime sa valeurs 

    def __len__(self):
        """Cette méthode est appelée quand on veut savoir la longueur de notre dictionnaire"""
        return len(self._dictionnaire)#On renvoit la longueur du dictionnaire
    
    def __add__(self, autre_objet):
        """On renvoie un nouveau dictionnaire contenant les deux
        dictionnaires mis bout à bout (d'abord self puis autre_objet)"""
        
        if type(autre_objet) is type(self):
            raise TypeError( \
                "Impossible de concaténer {0} et {1}".format( \
                type(self), type(autre_objet)))
        else:
            nouveau = DictionnaireOrdonne()
            
            # On commence par copier self dans le dictionnaire
            for cle, valeur in self.items():
                nouveau._dictionnaire[cle] = valeur
            
            # On copie ensuite autre_objet
            for cle, valeur in autre_objet.items():
                nouveau._dictionnaire[cle] = valeur
            return nouveau
    def sort(self):
        """Méthode appelée lorsqu'on veut trier notre dictionnaire"""
        sortedByKey = {k: v for k, v in sorted(self._dictionnaire.items())}#On crée un dictionnaire trié utilisant les clefs et 
        #les valeurs du dictionnaire d'origine
        self._dictionnaire = sortedByKey#On copie ce dictionnaire dans celui d'origine
        self.keyList = list(self._dictionnaire)#On copie les clefs
        self.valList = list(self._dictionnaire.values())#On copie les valeurs
        return self._dictionnaire
    
    def reverse(self):
        """Méthode appelée lorsqu'on veut trier notre dictionnaire dans le sens inverse"""
        sortedByKey2 = {k: v for k, v in sorted(self._dictionnaire.items(), reverse=True)}#On crée un dictionnaire trié le sens inverse 
        #utilisant les clefs et les valeurs du dictionnaire d'origine
        self._dictionnaire = sortedByKey2#On copie ce dictionnaire dans celui d'origine
        self.keyList = list(self._dictionnaire)#On copie les clefs
        self.valList = list(self._dictionnaire.values())#On copie les valeurs
        return self._dictionnaire

    def keys(self):
        return "Vos clefs : \n {}".format(self.keyList) 

    def values(self):
        return "Vos Valeurs : \n {}".format(self.valList) 

    def items(self):
        return self._dictionnaire.items()

     
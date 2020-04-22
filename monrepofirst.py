# -*- coding: utf-8 -*-



class GitClass:
    """  Ajouter ce script sur mon répertoire de travail  """

    def __init__(self,nombre_membre):
        self.nombre_membre=nombre_membre

     
    def TypeEtreVivant(self):
        if self.nombre_membre ==2:
            print("On a affaire a une personne")
            return "Personne"
        elif self.nombre_membre ==4:
            print("On a affaire a une animal")
            return "Animal"
        else:
            print("On a affaire a un extraterrestre")
            return "extraterrestre"    

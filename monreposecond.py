# -*- coding: utf-8 -*-



class Point(object):
    """ Classe Point(). Un point est défini par ses coordonées : abscisse
    et ordonnée """
    def __init__(self,nom,abscisse,ordonnée):
        self.nom=nom
        self.abscisse=abscisse
        self.ordonnée=ordonnée
        
    def __str__(self):
        return "{0}({1},{2})".format(self.nom,self.abscisse,self.ordonnée)

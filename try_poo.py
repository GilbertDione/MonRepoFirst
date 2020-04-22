# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:09:19 2020

@author: dell
"""




class Personne:
    age=0
    nom=''
    prenom=''




class Vecteur3D:
    def __init__(self,x0,y0,z0):
        self.x=x0
        self.y=y0
        self.z=z0
        
    def  __str__(self): #Affichage d'un vecteur3D
        return "Vecteur3D({:g},{:g},{:g})".format(self.x,self.y,self.z)
    
    
    # Sans cette methode, si on a : v1=Vecteur3D(3,6,4)
    # alors print(v1) donne <__main__.Vecteur3D object at 0x0000017D638C8988>
    # Mais avec cette methode, print(v1) donne Vecteur3D(3,6,4)
    def __add__(self, vector):
        return Vecteur3D(self.x+vector.x, self.y+vector.y, self.z+vector.z)
    
        
    def __mul__(self, vector):
        return Vecteur3D(self.x*vector.x, self.y*vector.y, self.z*vector.z)
    
    
    def __neg__(self):
        return Vecteur3D(-self.x, -self.y, -self.z)
    
    #def Afficher_Vecteur(self):
        #print ("Vecteur3D({:g},{:g},{:g})".format(self.x,self.y,self.z))
    #def Dertimant(self):
    
    
   
    
class LinearCode(object):
    """Code lineaire: un code lineaire est defini par sa dimension et sa longueur.
    """
    def __init__(self,dimension,length):
        self.dimension=dimension
        self.length=length
        self.test_var=0
        
        
        
    def __str__(self):
        return "LinearCode({0}, {1})".format(self.dimension,self.length)
        
    def affiche_code_params(self):
        print("La dimension et la longueur du code sont respectivement: {0} et"
              " {1} ".format(self.dimension,self.length))
    
    
class Hammingcode(LinearCode):
    """ Un code de Hamming est un code lineaire avec un seul parametre r.

        dimension=2r-r-1 et de longueur=2r-1        """
        
    def __init__(self,param):
        LinearCode.__init__(self,param,param)
        #Cet appel est nécessaire, afin que les objets de la classe HammingCode soient
        #initialisés de la même manièreque les objets de la classe LinearCode. 
        #Si nous n’effectuons pas cet appel, les objets-ions n’hériteront
        #pas automatiquement l'attribut test.var par exemple car ceux ci sont des attributs
        #d’instance créés par la méthode constructeur de la classe LinearCode()
        #et celle-ci n’est pas invoquée automatiquement lorsqu’on instancie 
        #des objets d’une classe dérivée.
        self.param=param
        self.dimension=2*self.param - self.param - 1
        self.length=2*self.param - 1
        
    def affiche_code_params(self): #Surcharge de cette methode 
        LinearCode.affiche_code_params(self) 
        
        #Lorsque dans la définition d’une classe, on souhaite faire appel à une méthode
        #définie dans une autre classe, il suffit de l’invoquer directement, via cette autre
        #classe, en lui transmettant la référence de l’instance comme premier argument
        # EXEMPLE : LinearCode.affiche_code_params(self) 
        # Dans cette instruction, self est bien entendu la référence de l’instance courante.
        # L'instance de HammingCode
        
        
        
   # RETENONS : Dans la méthode constructeur d’une classe dérivée, il faut presque toujours
   #prévoir un appel à la méthode constructeur de sa classe parente     
  

 
                 
        
   
    
"""      Modules contenant des bibliothèques de classes:

        if __name__ == "__main__":
            Code = HammingCode(4)
            print(Code)
            Code.ffiche_code_params()
            
            

        """
        #placée à la fin du module, elle sert à déterminer si le module est « lancé » en 
        #tant que programme autonome (auquel cas les instructions qui suivent doivent 
        #être exécutées), ou au contraire utilisé comme une bibliothèque de classes 
        #importée ailleurs. Dans ce cas cette  partie du code est sans effet
    
            
    
    

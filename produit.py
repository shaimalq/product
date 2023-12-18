
class Composition:
    def _init_(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite

    @property
    def produit(self):
        return self.__produit

    @produit.setter
    def produit(self, value):
        self.__produit = value

    @property
    def quantite(self):
        return self.__quantite

    @quantite.setter
    def quantite(self, value):
        self.__quantite = value


    def __str__(self) :
        return f"le produit:{self.__produit} ,la quantite :{self.__quantite}"
        
    def __eq__(self,other) -> bool:
        if isinstance(other,Composition):
            return self.__produit == other.__produit()
        

        

from abc import ABCMeta,abstractmethod

class Produit:
    def _init_(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def nom(self):
        return self.__nom
   
    @property
    def code(self):
        return self.__code
    @property
    def PrixHT(self):
        pass


class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super()._init_(nom, code)
        self.__prixAchat = prixAchat

    def _str_(self):
        return f"Produit élémentaire: {self.nom} (Code: {self.code}), Prix Achat: {self.__prixAchat}"

    def getPrixHT(self):
        return self.__prixAchat


from abc import abstractmethod
class ProduitCompose(Produit):
    tauxTVA = 0.18

    def _init_(self, nom, code, fraisFabrication):
        super()._init_(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants = []

    @property
    def fraisFabrication(self):
        return self.__fraisFabrication
    
    @property
    def listeConstituants(self):
        return self.__listeConstituants

    def _str_(self):
        return f"Produit composé: {self.nom} (Code: {self.code}), Frais de Fabrication: {self.__fraisFabrication}"
    @abstractmethod
    def getPrixHT(self):
        prixHT = sum(compo.produit.getPrixHT() * compo.quantite for compo in self.__listeConstituants)
        return prixHT + self.__fraisFabrication



class Livre:
    def __init__(self, id, titre, auteur, image, contenue ):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.image = image
        self.contenue = contenue
    
    def delete(self):
        self.id = None
        self.titre = None
        self.auteur = None
        self.image = None
        self.contenue = None

    def voir(self):
        return self.contenue
    
    def setTitre(self, titre):
        self.titre = titre

    def setAuteur(self, auteur):
        self.auteur = auteur

    def setImage(self, image):
        self.image = image
    
    def setContenue(self, contenue):
        self.contenue = contenue

    def getTitre(self):
        return self.titre
    
    def getAuteur(self):
        return self.auteur
    
    def getImage(self):
        return self.image
    
    def getContenue(self):
        return self.contenue
    


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def add_livre(self, livre):
        self.livres.append(livre)
    
    def liste(self):
        return self.livres
    
    def delete_livre(self, id):
        for livre in self.livres:
            if livre.id == id:
                self.livres.remove(livre)
                return True
        return False
    
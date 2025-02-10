import jsonpickle

class Livre:
    def __init__(self, id, titre, ):
        self.__id = id
        self.__titre = titre
        self.__auteur = input("Entrez l'auteur: ")
        self.__image = input("Entrez l'image : ")
        self.__contenue = input("Entrez le contenue: ")

    def delete(self):
        self.__id = None
        self.__titre = None
        self.__auteur = None
        self.__image = None
        self.__contenue = None

    def voir(self):
        return self.__contenue

    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setImage(self, image):
        self.__image = image

    def setContenue(self, contenue):
        self.__contenue = contenue

    def get_id(self):
        return self.__id

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_image(self):
        return self.__image

    def get_contenue(self):
        return self.__contenue

class Bibliotheque:
    def __init__(self):
        self.__livres = []

    def add_livre(self, livre):
        self.__livres.append(livre)

    def liste(self):
        return self.__livres

    def delete_livre(self, id):
        for livre in self.__livres:
            if livre.get_id() == id:
                self.__livres.remove(livre)
                return True
        return False

    def get_livre(self, id):
        for livre in self.__livres:
            if livre.get_id() == id:
                return livre
        return None

    def get_last_id(self):
        if self.__livres:
            return self.__livres[-1].get_id() + 1
        else:
            return 1


def charger_bibliotheque():
    try:
        with open('bibl.json', 'r') as json_file:
            contenu = json_file.read().strip()
            if not contenu:
                return Bibliotheque()
            return jsonpickle.decode(contenu)
    except FileNotFoundError:
        return Bibliotheque()

bibliotheque = charger_bibliotheque()
input_user = ""


def process_truc():
    global input_user
    if input_user == "rl":
        for livre in bibliotheque.liste():
            print("id : ", livre.get_id(), "titre : ", livre.get_titre(), "auteur : ", livre.get_auteur(), "image : ", livre.get_image(), "contenue : ", livre.get_contenue())

    elif input_user.startswith("al"):
        livre = Livre(bibliotheque.get_last_id(), input_user[3:])
        bibliotheque.add_livre(livre)

    elif input_user.startswith("vl"):
        livre = bibliotheque.get_livre(int(input_user[3:]))
        if livre:
            print("id : ", livre.get_id(), "titre : ", livre.get_titre(), "auteur : ", livre.get_auteur(), "image : ", livre.get_image(), "contenue : ", livre.get_contenue())
        else:
            print("Livre non trouvé")

    elif input_user.startswith("dl"):
        if bibliotheque.delete_livre(int(input_user[3:])):
            print("Livre supprimé")
        else:
            print("Livre non trouvé")

    elif input_user.startswith("c"):
        livre = bibliotheque.get_livre(int(input_user[2:]))
        if livre:
            livre.setContenue(input("Entrez le nouveau contenu: "))
        else:
            print("Livre non trouvé")

    elif input_user.startswith("t"):
        livre = bibliotheque.get_livre(int(input_user[2:]))
        if livre:
            livre.setTitre(input("Entrez le nouveau titre: "))
        else:
            print("Livre non trouvé")

    elif input_user.startswith("w"):
        livre = bibliotheque.get_livre(int(input_user[2:]))
        if livre:
            livre.setAuteur(input("Entrez le nouvel auteur: "))
        else:
            print("Livre non trouvé")

    elif input_user.startswith("i"):
        livre = bibliotheque.get_livre(int(input_user[2:]))
        if livre:
            livre.setImage(input("Entrez la nouvelle image: "))
        else:
            print("Livre non trouvé")


if __name__ == '__main__':
    while input_user != "exit":
        print("")
        print("taper rl pour afficher la liste des livres")
        print("taper al + nom pour ajouter un livre")
        print("taper vl + id pour voir un livre")
        print("taper dl + id pour supprimer un livre")
        print("taper c + id pour changer le contenu d'un livre")
        print("taper t + id pour changer le titre d'un livre")
        print("taper w + id pour changer l'auteur d'un livre")
        print("taper i + id pour changer l'image d'un livre")
        print("taper exit pour quitter")
        input_user = input("Entrez un truc: ")
        print("")
        process_truc()
        with open('bibl.json', 'w') as json_file:
            json_file.write(jsonpickle.encode(bibliotheque))  
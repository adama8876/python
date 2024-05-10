from enum import Enum

class Role(Enum):
    Admin = "Admin"
    Personnel = "Personnel"
    Client = "Client"

class Users:
    def __init__(self, idUser, nom, prenom, mot_de_passe, téléphone, role):
        self.idUser = idUser
        self.nom = nom
        self.prenom = prenom
        self.mot_de_passe = mot_de_passe
        self.téléphone = téléphone
        self.role = role
    
    def Ajouter_utilisateur(self):
        # Logique pour ajouter un utilisateur
        print("Utilisateur ajoute :", "prenom:",self.prenom, "nom:",self.nom, "mdp:", self.mot_de_passe, "phone:", self.téléphone)
    
    def Supprimer_utilisateur(self):
        # Logique pour supprimer un utilisateur
        print("Utilisateur supprime :", self.prenom, self.nom)

# Création d'une instance de la classe Users
user = Users(1, "Samake", "Bakary", "123456", "83-93-88-76", Role.Client)

# Appel de la méthode Ajouter_utilisateur()
user.Ajouter_utilisateur()

# Appel de la méthode Supprimer_utilisateur()
user.Supprimer_utilisateur()
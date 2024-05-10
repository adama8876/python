from datetime import date

class Commande:
    def __init__(self, id_commande, date, status, quantiteCommande):
        self.id_commande = id_commande
        self.date = date
        self.status = status
        self.quantiteCommande = quantiteCommande
    
    def Ajouter_cmd(self):
        # Logique pour ajouter une commande
        print("Commande ajoutée :", self.id_commande)
    
    def Modifier_cmd(self):
        # Logique pour modifier une commande
        print("Commande modifiée :", self.id_commande)
    
    def Supprimer_cmd(self):
        # Logique pour supprimer une commande
        print("Commande supprimée :", self.id_commande)
    
    def parcourir(self):
        # Logique pour parcourir les commandes
        print("Parcours des commandes...")
        print("Commande :", self.id_commande)
        print("Date :", self.date)
        print("Statut :", self.status)
        print("Quantité de commande :", self.quantiteCommande)

# Création d'une instance de la classe Commande
commande = Commande(1, date.today(), "En cours", 10)

# Appel de la méthode Ajouter_cmd()
commande.Ajouter_cmd()

# Appel de la méthode Modifier_cmd()
commande.Modifier_cmd()

# Appel de la méthode Supprimer_cmd()
commande.Supprimer_cmd()

# Appel de la méthode parcourir()
commande.parcourir()
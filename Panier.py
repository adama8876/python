class Panier :
    def __init__(self, id_Panier, Total_Panier=0.0, Etat_Panier=False):
        self.id_Panier = id_Panier
        self.Total_Panier = Total_Panier
        self.Etat_Panier = Etat_Panier
    
    def Ajouter_Produit(self, quantite, prix_unitaire):
        self.Total_Panier += quantite * prix_unitaire
    
    def MiseajourQteProduit(self, quantite, prix_unitaire):
        self.Total_Panier -= quantite * prix_unitaire
    
    def getTotalPanier(self):
        return self.Total_Panier

# Création d'une instance de la classe Panier avec un autre nom d'objet
mon_panier = Panier(1)

# Ajouter des produits au panier
mon_panier.Ajouter_Produit(2, 1000)
mon_panier.Ajouter_Produit(3, 800)

# Mettre à jour la quantité d'un produit existant
mon_panier.MiseajourQteProduit(1, 1000)

# Obtenir le total du panier
total = mon_panier.getTotalPanier()
print("Total du panier:", total)
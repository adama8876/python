class Categorie:
    def __init__(self, id_categorie, nom):
        self.id_categorie = id_categorie
        self.nom = nom

    def Ajouter_cat(self):
        print("Catégorie ajoutée :", self.nom)

    def Modifier_cat(self):
        print("Catégorie modifiée :", self.nom)

    def Supprimer_cat(self):
        print("Catégorie supprimée :", self.nom)


# Bloc de tests fonctionnels
if __name__ == "__main__":
    # Test de la méthode Ajouter_cat()
    categorie1 = Categorie(1, "Vêtements pour dames")
    categorie1.Ajouter_cat()  
    # Test de la méthode Modifier_cat()
    categorie1.nom = "Vêtements pour femmes et enfants"
    categorie1.Modifier_cat()  
    # Test de la méthode Supprimer_cat()
    categorie1.Supprimer_cat()  
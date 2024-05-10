class Notification:
    def __init__(self, id_notification, message):
        self.id_notification = id_notification
        self.message = message
    
    def envoyerMessage(self):
        print("Message :", self.message)

        # Création d'une instance de la classe Notification
notification1 = Notification(1, " Vous avez payé la commande N°0011 au prix TTC de 23000 F CFA !")

# Appel de la méthode envoyerMessage()
notification1.envoyerMessage()
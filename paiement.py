from datetime import date

class Payement:
    def __init__(self, id_payement, mode_payement, date_reglement, montant_paye):
        self.id_payement = id_payement
        self.mode_payement = mode_payement
        self.date_reglement = date_reglement
        self.montant_paye = montant_paye
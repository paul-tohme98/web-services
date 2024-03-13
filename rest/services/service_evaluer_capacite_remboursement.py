class CapaciteRemboursement():
    @classmethod
    def eval_capacite_remboursement(ctx, revenus, depenses):
        try:
            # Calculer le solde mensuel (revenus - dépenses)
            solde_mensuel = revenus - depenses
        
            # Vérifier la capacité de remboursement en fonction du solde
            if solde_mensuel > 0:
                capacite_remboursement = "Le client a une capacité de remboursement positive."
            elif solde_mensuel == 0:
                capacite_remboursement = "Le client a juste assez de revenus pour couvrir ses dépenses."
            else:
                capacite_remboursement = "Le client a un solde négatif. Il peut avoir des difficultés à rembourser ses dettes."
        
            return capacite_remboursement
        except Exception as e:
            return "Error occured while evaluating capacity"
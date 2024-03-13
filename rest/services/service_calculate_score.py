class CalculateScore():
    @classmethod
    def calculate_loan_score(ctx, dettes_en_cours, paiement_en_retard, antecedent_faillite):
        try:
            # Logique pour calculer le score en fonction de l'historique financier
            # Ceci est une logique de démonstration, veuillez ajuster selon vos besoins
            score = 100  # Score initial

            if dettes_en_cours > 5000:
                score -= 10

            if paiement_en_retard > 0:
                score -= 20

            if antecedent_faillite:
                score -= 50

            return score
        except Exception as e:
            return "An error has occured while calculating the score"
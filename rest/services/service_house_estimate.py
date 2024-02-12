from statistics import mean

class HouseEstimate():
    def house_estimated_value(ctx, input_list):
        try:
            # Vérifier que la liste n'est pas vide
            if not input_list:
                raise ValueError("Pas de biens similaires trouvés.")

            # Exemple simple : Somme des valeurs de la liste
            valEstimee = mean(input_list)

            # Vous pouvez ajouter une logique plus complexe ici en fonction de vos besoins

            return valEstimee
        except Exception as e:
            return "error occured while estimating house value"
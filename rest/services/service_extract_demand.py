import json


class ExtractDemand():
    def process_txt_file(ctx, file_content, file_path):
        try:
            # Read the content of the text file
            with open(file_path, 'r') as file:
                file_content = file.read()

            # Process the file content as before
            lines = file_content.split('\n')

            # Initialize variables to store information
            nom = ""
            email = ""
            adresse = ""
            numero = ""
            duree = ""
            description = ""
            montant = 0.00
            adresseMaison = ""
            prixMaison = 0.00

            # Iterate through each line to extract information
            for line in lines:
                if "Nom du client: " in line:
                    nom = line.split("Nom du client: ")[1].strip()
                if "Adresse: " in line:
                    adresse = line.split("Adresse: ")[1].strip()
                if "Email: " in line:
                    email = line.split("Email: ")[1].strip()
                if "Numéro de téléphone: " in line:
                    numero = line.split("Numéro de téléphone: ")[1].strip()
                if "Durée du prêt: " in line:
                    duree = line.split("Durée du prêt: ")[1].split("ans")[0].strip()
                if "Description de la propriété: " in line: 
                    description = line.split("Description de la propriété: ")[1].strip()
                if "Montant du prêt demandé:" in line:
                    montant_str = line.split("Montant du prêt demandé: ")[1].split("EUR")[0].strip()
                    montant = float(montant_str)
                if "Adresse maison:" in line:
                    adresseMaison = line.split("Adresse maison: ")[1].strip()
                if "Prix maison:" in line:
                    prixMaison_str = line.split("Prix maison: ")[1].split("EUR")[0].strip()
                    prixMaison = int(prixMaison_str)
                    
            
            # Create a JSON object with the extracted information
            data = {
                "nom" : nom,
                "email" : email,
                "adresse" : adresse,
                "numero" : numero,
                "duree" : duree,
                "description" : description,
                "montant" : montant,
                "adresseMaison" : adresseMaison,
                "prixMaison" : prixMaison
            }

            # Convert the JSON object to a string
            result = json.dumps(data)      
            
            return result
        except Exception as e:
            return "An error occurred while processing the file."
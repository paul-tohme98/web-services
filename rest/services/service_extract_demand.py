import json
from fastapi import HTTPException
import requests

class ExtractDemand():
    @classmethod
    def process_txt_file(ctx, file_content, file_path):
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
            if "Numero de telephone: " in line:
                numero = line.split("Numero de telephone: ")[1].strip()
            if "Duree du pret: " in line:
                duree = line.split("Duree du pret: ")[1].split("ans")[0].strip()
            if "Description de la propriete: " in line: 
                description = line.split("Description de la propriete: ")[1].strip()
            if "Montant du pret demande:" in line:
                montant_str = line.split("Montant du pret demande: ")[1].split("EUR")[0].strip()
                print("Extracted montant_str:", montant_str)  # Add this line for debugging
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

        # Determine the directory of the input file
        #input_directory = os.path.dirname(file_path)

        # Construct the output file path in the same directory
        #output_file_path = os.path.join(input_directory, "output.json")

        # Write the JSON result to the output file
        #with open(output_file_path, 'w') as output_file:
        #    output_file.write(result)            
        
        return result
    



# file_content = "BASE64_ENCODED_CONTENT"
# result = ExtractDemand.process_txt_file(file_content, "C:/Users/pault/Documents/WebServices/rest/demands/client_1.txt")
# print (result)


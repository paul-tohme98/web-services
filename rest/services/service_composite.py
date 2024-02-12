import json
from functions.call_extract_file import call_extract_demand_api
from functions.database_connection import DatabaseConnection

class ServiceComposite():
    @classmethod
    def controller(self, filepath):
        try:
            extract_demand = call_extract_demand_api(filepath=filepath)

            # Check if the API call was successful
            if "error" in extract_demand:
                print("Error:", extract_demand["error"])
                return

            # Parse the JSON response
            result_json = extract_demand["result"]
            result_dict = json.loads(result_json)

            # Access and print specific values
            nom = result_dict.get("nom", "N/A")
            email = result_dict.get("email", "N/A")
            adresse = result_dict.get("adresse", "N/A")
            numero = result_dict.get("numero", "N/A")
            duree = result_dict.get("duree", "N/A")
            description = result_dict.get("description", "N/A")
            montant = result_dict.get("montant", "N/A")
            adresseMaison = result_dict.get("adresseMaison", "N/A")
            prixMaison = result_dict.get("prixMaison", "N/A")

            print("Demand chosen:", filepath)
            print("Nom:", nom)
            print("Email:", email)
            print("Adresse:", adresse)
            print("Numero:", numero)
            print("Duree:", duree)
            print("Description:", description)
            print("Montant:", montant)
            print("Adresse Maison:", adresseMaison)
            print("Prix Maison:", prixMaison)

            db = DatabaseConnection()
            print("Connecting...")
            [conn, cursor] = db.openConnection()
            print("Connection opened")
            db.closeConnection(conn=conn, cursor=cursor)
            print("Connection closed")

            return
        except Exception as e:
            return "Error occurred in the controller: " + str(e)

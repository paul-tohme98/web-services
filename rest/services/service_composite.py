import datetime
import json
from services.service_extract_demand import ExtractDemand
from api import *

class ServiceComposite():
    @classmethod
    async def controller(cls, filepath, filecontent):
        # Process the text file content to extract demand information
        extract_demand = ExtractDemand.process_txt_file(filecontent, filepath)

        # Check if there was an error during extraction
        if "error" in extract_demand:
            print("Error:", extract_demand["error"])
            return

        # Parse the JSON response directly, no need to call `extract_demand` again
        result_dict = json.loads(extract_demand)
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

        client_id = await get_client_id(email)
        print("Client ID : ", client_id)

        house_props = await get_house_props(adresseMaison)
        print("House props : ", house_props)

        house_id = house_props[0]

        house_addr = house_props[10]
        house_est_val = house_props[2]
        house_area = house_props[3]
        house_nb_chambers = house_props[4]
        house_region = house_props[9]

        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        date_demand = current_date.strftime("%Y-%m-%d")
        print("INSERTING...........")

        await insert_demand(client_id, montant, duree, house_id, date_demand, 0)
        print("Demand inserted!")

        loan_score = await calculate_score(client_id)
        print("Loan score : ", loan_score)

        capacite_remboursement = await calculate_capacity(client_id)
        print("Capacite de remboursement : ", capacite_remboursement)
        
        if capacite_remboursement == "Le client a une capacité de remboursement positive.":
            isAllowed = True
        else:
            isAllowed = False

        est_prop = await house_estim(house_region, house_addr, house_area, house_nb_chambers)

        

        # Process the result

        verify_conf = await prop_conform(house_id)

        print("Loan score : ", loan_score)
        print("Analyse revenues and depenses : ", capacite_remboursement)
        print("House price estimate : ", est_prop)
        print("Le bien est-il conforme ?? : ", verify_conf)
        print("Is allowed : ", isAllowed)

            # In your controller method:
        if isinstance(est_prop, dict):
            print("Not in the right format")
            return False
        else:
            print("isAllowed : ", isAllowed)
            print("Verify conf : ", verify_conf)
            print("Loan score : ", loan_score)
            print("House est val : ", house_est_val)
            thresh = est_prop - 100000
            print("Thresh : ", thresh)
            # Proceed with the calculation
            if isAllowed and verify_conf and loan_score >= 20 and house_est_val >= (est_prop - 100000):
                result = True
            else:
                result = False

            return result

        #return result


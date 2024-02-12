from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import random


from services.service_extract_demand import ExtractDemand
from services.service_calculate_score import CalculateScore
from services.service_evaluer_capacite_remboursement import CapaciteRemboursement
from services.service_prop_conforme import PropConforme
from services.service_house_estimate import HouseEstimate

class User(BaseModel):
	name: str
	age: Optional[int] = None
	gender: str
	phone: Optional[str] = None


app = FastAPI()

# Server Up
@app.get("/")
async def root():
	return {"message": "Server is Up!"}

# Extract and process the demand
@app.get("/extract-demand/")
async def extract_demand(filepath: str):
    ext_demand = ExtractDemand()

    try:
        # Read and process the text file
        with open(filepath, "r") as file:
            file_content = file.read()
            result = ext_demand.process_txt_file(file_path=filepath, file_content=file_content)
        return {"result": result}
    except FileNotFoundError:
        return {"error": "File not found"}
    except Exception as e:
        return {"error": str(e)}

# Calculate score
@app.get("/calculate-score/")
async def calculate_score(dettes_en_cours: int, paiement_en_retard: int, antecedent_faillite: int):
    try:
        calc_score = CalculateScore()
        result = calc_score.calculate_loan_score(dettes_en_cours=dettes_en_cours, paiement_en_retard=paiement_en_retard, antecedent_faillite=antecedent_faillite)
        return result
    except Exception as e:
        return {"error": str(e)}
	
# Evaluer la capacite de remboursement
@app.get("/capacite-remboursement/")
async def eval_capacite_remboursement(depenses: int, revenus: int):
      try:
            capacite_remboursement = CapaciteRemboursement()
            result = capacite_remboursement.eval_capacite_remboursement(depenses=depenses, revenus=revenus)
            return result
      except Exception as e:
            return {"error": str(e)}

# Verifier la conformite de la maison
@app.get("/house-conformity")
async def prop_conform(land_dispute: bool, complies_with_regulations: bool, eligible_for_loan: bool):
      try:
            conformity = PropConforme()
            result = conformity.verify_conf_house(land_dispute=land_dispute, complies_with_regulations=complies_with_regulations, eligible_for_loan=eligible_for_loan)
            return result
      except Exception as e:
            return {"error": str(e)}

# Estimate house value
@app.get("/house-estimated-value/")
async def house_estim(input_list: list):
      try:
            estimation = HouseEstimate()
            estimation.house_estimated_value(input_list=input_list)
      except Exception as e:
            return {"error": str(e)}

# Parametres de requete
@app.get("/user/")
async def create_user_id(start: int, end: int):
	return {"user id" : random.randint(start, end)}
# for example : http://127.0.0.1:8000/user/?start=1&end=10

@app.post("/user/")
async def create_user(user: User):
	return user

# Data conversion and validation
@app.get("/user/id/{id}")
async def read_name(id: int):
	return {"user id" : id}


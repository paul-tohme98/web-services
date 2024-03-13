from fastapi import FastAPI, HTTPException
from typing import Optional
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import random


from services.service_extract_demand import ExtractDemand
from services.service_calculate_score import CalculateScore
from services.service_evaluer_capacite_remboursement import CapaciteRemboursement
from services.service_prop_conforme import PropConforme
from services.service_house_estimate import HouseEstimate

from queries.database_connection import DatabaseConnection

class User(BaseModel):
	name: str
	age: Optional[int] = None
	gender: str
	phone: Optional[str] = None


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_database = os.environ.get("DB_DATABASE")

app = FastAPI()

# Server Up
@app.get("/")
async def root():
	return {"message": "Server is Up!"}

@app.get("/db-connect")
async def connect_database():

    conn, cursor = DatabaseConnection.openConnection(db_host, db_user, db_password, db_database)
    if(conn):
        print("Connection established")
        return "Connection established"
    else:
         return "Connection Failed!"


# Extract and process the demand
@app.get("/extract-demand")
async def extract_demand(filepath: str, filecontent: str):
    try:
        # Call the ExtractDemand process_txt_file method to process the file content
        result = ExtractDemand.process_txt_file(filepath, filecontent)
        return result
    except Exception as e:
        # Raise an HTTPException with a status code of 500 and the error message
        raise HTTPException(status_code=500, detail=str(e))

# Calculate score
@app.get("/calculate-score/")
async def calculate_score(client_id : str):
    try:
        conn, cursor = DatabaseConnection.openConnection(db_host, db_user, db_password, db_database)
        [dettes_en_cours, paiement_en_retard, antecedent_faillite] = DatabaseConnection.getDataForLoanScore(cursor, client_id)
        
        result = CalculateScore.calculate_loan_score(dettes_en_cours=dettes_en_cours, paiement_en_retard=paiement_en_retard, antecedent_faillite=antecedent_faillite)
        return result
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/capacite-remboursement")
async def calculate_capacity(client_id : str):
    conn, cursor = DatabaseConnection.openConnection(db_host, db_user, db_password, db_database)
    [revenus, depenses] = DatabaseConnection.getRevenuData(cursor, client_id)
    result = CapaciteRemboursement.eval_capacite_remboursement(depenses=depenses, revenus=revenus)
    return result

# Verifier la conformite de la maison
@app.get("/house-conformity")
async def prop_conform(house_id : int):
      try:
            conn, cursor = DatabaseConnection.openConnection(db_host, db_user, db_password, db_database)
            [land_dispute, complies_with_regulations, eligible_for_loan] = DatabaseConnection.getConformityData(cursor, house_id)
            result = PropConforme.verify_conf_house(land_dispute=land_dispute, complies_with_regulations=complies_with_regulations, eligible_for_loan=eligible_for_loan)
            return result
      except Exception as e:
            return {"error": str(e)}

# Estimate house value
@app.get("/house-estimated-value")
async def house_estim(region : str, codePostal : str, surface : float, nbChambres : int):
    try:
        conn, cursor = DatabaseConnection.openConnection(db_host, db_user, db_password, db_database)
        input_list = DatabaseConnection.getEstimation(cursor, region, codePostal, surface, nbChambres)
        if 'error' in input_list:
            return {"error": input_list['error']}
        estimatedValue = HouseEstimate.house_estimated_value(input_list=input_list)
        return estimatedValue
    except Exception as e:
        return {"error": str(e)}


@app.get("/user_id")
async def get_client_id(email : str):
    conn, cursor = DatabaseConnection.openConnection(db_host, db_user, db_password, db_database)
    client_id = DatabaseConnection.getClientId(cursor, email)
    DatabaseConnection.closeConnection(conn, cursor)
    return client_id[0]

@app.get("/house-id")
async def get_house_props(address : str):
    conn, cursor = DatabaseConnection.openConnection(db_host, db_user, db_password, db_database)
    house_props = DatabaseConnection.getHouseProps(cursor, address)
    return house_props
     

# Insert demand into database
@app.post("/insert-demand/")
async def insert_demand(client_id: int, loan_amount: int, loan_duration: int, house_id: int, date_demand: str, valid: int):
    try:
        # Open a database connection
        conn, cursor = DatabaseConnection.openConnection(db_host, db_user, db_password, db_database)
        print("DATA", client_id, int(loan_amount), int(loan_duration), house_id, str(date_demand), valid)
        # Call the insertDemand method
        DatabaseConnection.insertDemand(conn, cursor, client_id, int(loan_amount), int(loan_duration), house_id, str(date_demand), valid)

        # Close the database connection
        # DatabaseConnection.closeConnection(conn, cursor)

        return {"message": "Demand inserted successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import uvicorn
# from decouple import Config
from api import app  # Import your FastAPI app
from queries.database_connection import DatabaseConnection
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access environment variables using os.environ.get()
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_DATABASE')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

# Start server
if __name__ == "__main__":
    try:
        print("Hello")
        DatabaseConnection.openConnection(db_host, db_user, db_password, db_name)
        uvicorn.run(app, host=db_host, port=8080)
    except Exception as e:
        print(e)

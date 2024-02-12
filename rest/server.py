import uvicorn
# from decouple import Config
from api import app  # Import your FastAPI app



# Start server
if __name__ == "__main__":
    try:
        # config = Config('.env')
        # port = config.get('PORT')
        # address = config.get('ADDRESS')
        uvicorn.run(app, host='127.0.0.1', port=8080)
    except Exception as e:
        print(e)

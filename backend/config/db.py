import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

def connectDB():
    load_dotenv()
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_URI = DATABASE_NAME.replace("<db_password>", DATABASE_PASSWORD)
    try:
        client = MongoClient(DATABASE_URI, serverSelectionTimeoutMS=5000)  # 5 sec timeout
        
        client.admin.command("ping")
        
        print("DB Connected Successfully!")
        db = client["MachineSensorsDB"]
        return db["machines"]
    except (ConnectionFailure, ServerSelectionTimeoutError) as e:
        print(f"MongoDB Connection Failed: {e}")
        return None
machinesCollection = connectDB()
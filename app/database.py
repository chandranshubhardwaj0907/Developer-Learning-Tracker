import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")



client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

goals_collection = database.get_collection("goals")
sessions_collection = database.get_collection("sessions")
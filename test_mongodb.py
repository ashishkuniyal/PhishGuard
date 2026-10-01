import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load variables from .env
load_dotenv()

# Get MongoDB URL from .env
uri = os.getenv("MONGO_DB_URL")

if not uri:
    raise ValueError("MONGO_DB_URL is not configured in .env")

# Create MongoDB client
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB Atlas!")

    print("Server:", client.address)

except Exception as e:
    print("MongoDB connection error:", e)
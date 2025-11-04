import motor.motor_asyncio
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Force local MongoDB connection for development
MONGODB_URI = "mongodb://localhost:27017"
DB_NAME = "mealcraft"

class DatabaseModule:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        """Establish MongoDB Atlas connection."""
        self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
        self.db = self.client[DB_NAME]
        print(f"✅ Connected to MongoDB: {DB_NAME}")

    async def disconnect(self):
        """Disconnect MongoDB client."""
        if self.client:
            self.client.close()
            print("❎ MongoDB connection closed.")

# Global instance
db_module = DatabaseModule()

# Dependency for FastAPI lifecycle events
async def connect_to_mongo():
    await db_module.connect()

async def close_mongo_connection():
    await db_module.disconnect()
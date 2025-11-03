from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.health import router as health_router
from app.core.database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="MealCraft AI Backend", version="0.1.0")

# Allow frontend origin (local dev and deploy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lifecycle events
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

# Include routers
app.include_router(health_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to MealCraft AI Backend"}
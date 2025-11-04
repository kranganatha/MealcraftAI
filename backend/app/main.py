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

# Lifecycle events removed for stateless operation

# Include routers
app.include_router(health_router, prefix="/api/v1")

# Replace all authentication behavior with a temporary session-free query handler
from fastapi import Request

@app.post("/api/v1/query")
async def handle_query(request: Request):
    data = await request.json()
    question = data.get("question", "")
    # Temporary in-memory response processing
    return {"answer": f"Temporary response for: '{question}' (no login required)."}

@app.get("/")
async def root():
    return {"message": "MealCraft AI Backend (stateless mode)"}
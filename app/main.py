# app/main.py

from fastapi import FastAPI
from app.routes import router
from app.database import init_db

app = FastAPI(title="Notification Service", version="1.0")

# Include router(s)
app.include_router(router)

# Run DB index creation on startup
@app.on_event("startup")
async def startup_event():
    await init_db()          

# Health check route
@app.get("/")
async def root():
    return {"message": "Notification Service is running"}
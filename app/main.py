
from fastapi import FastAPI
from app.routes import router
from app.database import init_db

app = FastAPI(title="Notification Service", version="1.0")


app.include_router(router)


@app.on_event("startup")
async def startup_event():
    await init_db()          

@app.get("/")
async def root():
    return {"message": "Notification Service is running"}
from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import get_db

app = FastAPI(
    title = "School Management System",
    description = "Multi-tenant school management system",
    version = "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
    "message": "School Management System API is running"
    }

@app.get("/api/v1/health/db")
def database_health(db:Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))

    return {
        "database" : "connected",
        "result" : result.scalar()
    }

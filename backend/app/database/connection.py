from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.database.base import Base

DATABASE_URL = URL.create(
    drivername = "postgresql+psycopg",
    username = settings.DB_USER,
    password = settings.DB_PASSWORD,
    host = settings.DB_HOST,
    port = settings.DB_PORT,
    database = settings.DB_NAME,
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False
)

SessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False,
    autocommit=False,
)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
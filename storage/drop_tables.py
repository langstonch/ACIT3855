from sqlalchemy import create_engine
from models import Base

DB_ENGINE = create_engine("sqlite:///telemetry.db")

if __name__ == "__main__":
    Base.metadata.drop_all(DB_ENGINE)
    print("Database tables dropped.")
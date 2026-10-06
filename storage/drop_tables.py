from sqlalchemy import create_engine
from models import Base

DB_ENGINE = create_engine(
    "mysql+pymysql://telemetry_user:telemetry_password@localhost:3307/telemetry_db"
)

if __name__ == "__main__":
    Base.metadata.drop_all(DB_ENGINE)
    print("Database tables dropped from telemetry_db.")

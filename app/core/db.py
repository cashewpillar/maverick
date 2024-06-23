from sqlmodel import SQLModel, create_engine
from app.core.config import settings

# Import models for when main.py calls metadata.create_all https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata-order-matters
from app import models

engine = create_engine(
  str(settings.SQLALCHEMY_DATABASE_URI), 
  echo=True if settings.ENVIRONMENT != "production" else False
)

def create_db_and_tables() -> None:
  SQLModel.metadata.create_all(engine)
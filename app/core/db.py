from sqlmodel import SQLModel, create_engine
from app import settings

# Import models for when main.py calls metadata.create_all https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata-order-matters
from .. import models 

# Remove echo=True in production (used here for learning and debugging)
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=True)
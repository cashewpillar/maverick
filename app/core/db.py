from sqlmodel import SQLModel, create_engine

# Import models for when main.py calls metadata.create_all https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata-order-matters
from .. import models 

sqlite_file_name = "maverick_dev.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Remove echo=True in production (used here for learning and debugging)
engine = create_engine(sqlite_url, echo=True)
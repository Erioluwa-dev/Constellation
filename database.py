from sqlmodel import create_engine
from sqlmodel import SQLModel
from models import Node, Edge

engine = create_engine("sqlite:///constellation.db")
SQLModel.metadata.create_all(engine)

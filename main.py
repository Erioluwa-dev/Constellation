from fastapi import FastAPI
from models import Node
from sqlmodel import Session
from database import engine


app = FastAPI(title="Constellation API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/nodes")
def create_node(node:Node):
    return {"node": "created"}

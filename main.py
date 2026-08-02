from fastapi import FastAPI
from sqlmodel import Session
from database import engine
from models import Node


app = FastAPI(title="Constellation API")

@app.get("/")
def main():
    return {"message": "welcome to Constellation"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/nodes")
def create_node(node: Node):
    with Session(engine) as session:
        session.add(node)
        session.commit()
        session.refresh(node)
        return node



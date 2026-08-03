from platform import node
from fastapi import HTTPException

from fastapi import FastAPI
from sqlalchemy.sql.roles import LimitOffsetRole
from sqlalchemy.sql.util import _offset_or_limit_clause
from sqlmodel import Session, select
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


@app.get("/nodes")
def list_nodes():
    with Session(engine) as session:
        nodes = session.exec(select(Node)).all()
        return nodes


@app.delete("/nodes/{node_id}")
def delete_nodes(node_id: int):
    with Session(engine) as session:
        node= session.get(Node, node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node not found")
            session.delete(node)
            session.commit()
            return {"Successful":"Deleted node"}


from fastapi import HTTPException
from fastapi import FastAPI
from sqlmodel import Session, select

from database import engine
from models import Node
from models import NodeUpdate
from models import Edge


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


@app.get("/nodes/{node_id}")
def get_specific_node(node_id: int):
    with Session(engine) as session:
        node= session.get(Node, node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node not found")
        return node


@app.patch("/nodes/{node_id}")
def update_node(node_id: int, node_update: NodeUpdate):
    with Session(engine) as session:
        node = session.get(Node, node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node not found")

        update_data = node_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(node, key, value)

        session.add(node)
        session.commit()
        session.refresh(node)
        return node



@app.delete("/nodes/{node_id}")
def delete_nodes(node_id: int):
    with Session(engine) as session:
        node= session.get(Node, node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node not found")
        session.delete(node)
        session.commit()
        return {"Successful":"Deleted node"}


#Edges

@app.post("/edges")
def create_edge(edge: Edge):
    with Session(engine) as session:
        session.add(edge)
        session.commit()
        session.refresh(edge)
        return edge


@app.get("/edges")
def list_edges():
    with Session(engine) as session:
        edge= session.exec(select(Edge)).all())
        return edge

@app.get("/edges/{edge_id}")
def list_specific_edge(edge_id: int):
    with Session(engine) as session:
        edge= session.get(Edge, edge_id)
        if not edge:
            raise HTTPException (status_code=404, detail="Edge not found")
        return edge

@app.delete("/edges/{edge_id}")
def delete_nodes(edge_id: int):
    with Session(engine) as session:
        edge= session.get(Edge, edge_id)
        if not edge:
            raise HTTPException(status_code=404, detail="Edge not found")
        session.delete(edge)
        session.commit()
        return {"Successful":"Deleted edge"}

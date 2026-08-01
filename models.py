from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Node(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    tags: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Edge(SqlModel, table=True):
    id: Optional[int]= Field(default=None , primary_key=True)
    source_id: int = Field(foreign_key="node.id")
    target_id: int = Field(foreign_key="node.id")
    shared_id: str

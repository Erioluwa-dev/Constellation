class Edge(SqlModel, table=True):
    id: Optional[int]= Field(default=None , primary_key=True)
    source_id: int = Field(foreign_key="node.id")
    target_id: int = Field(foreign_key="node.id")
    shared_id: str

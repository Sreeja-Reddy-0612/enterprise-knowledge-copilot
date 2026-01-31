from pydantic import BaseModel

class QueryInput(BaseModel):
    question: str
    knowledge_version: str

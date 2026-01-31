from pydantic import BaseModel

class DocumentInput(BaseModel):
    knowledge_version: str

from pydantic import BaseModel
from typing import List

class AnswerOutput(BaseModel):
    answer: str
    sources: List[str]
    knowledge_version: str

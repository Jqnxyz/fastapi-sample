from pydantic import BaseModel


class Prompt(BaseModel):
    query: str

from pydantic import BaseModel


class Prompt(BaseModel):
    query: str


class PromptResponse(BaseModel):
    query: str
    response: str

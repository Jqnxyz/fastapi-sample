from pydantic import BaseModel


class Prompt(BaseModel):
    id: int
    prompt: str | None = None

    class Config:
        orm_mode = True


class PromptCreate(BaseModel):
    prompt: str

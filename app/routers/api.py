from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from ..schemas.api import Prompt
from ..api import openai as OpenAI

from ..sql_app.crud import prompts as promptCrud
from ..sql_app.schemas import prompts as promptSchemas
from ..sql_app import models as promptModel
from ..sql_app.database import SessionLocal, engine

promptModel.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/prompt")
def prompt(prompt: Prompt):
    response = OpenAI.gpt_prompt(prompt.query)
    create_prompt(promptSchemas.PromptCreate(prompt=prompt.query))
    return response


def create_prompt(prompt: promptSchemas.PromptCreate):
    db = SessionLocal()
    return promptCrud.create_prompt(db=db, prompt=prompt)

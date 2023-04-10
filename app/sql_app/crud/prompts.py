from sqlalchemy.orm import Session

from .. import models as promptModel
from ..schemas import prompts as promptSchemas


def get_prompt(db: Session, id: int):
    return db.query(promptModel.Prompt).filter(promptModel.Prompt.id == id).first()


def create_prompt(db: Session, prompt: promptSchemas.PromptCreate):
    db_prompt = promptModel.Prompt(prompt=prompt.prompt)
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt

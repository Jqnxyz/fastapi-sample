from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .crud import prompts as promptCrud
from .schemas import prompts as promptSchemas
from .models import prompts as promptModel
from .database import SessionLocal, engine

promptModel.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/prompts/", response_model=promptSchemas.Prompt)
def create_prompt(prompt: promptSchemas.PromptCreate, db: Session = Depends(get_db)):
    return promptCrud.create_prompt(db=db, prompt=prompt)


@app.get("/prompts/{prompt_id}", response_model=promptSchemas.Prompt)
def read_prompt(prompt_id: int, db: Session = Depends(get_db)):
    db_prompt = promptCrud.get_prompt(db, id=prompt_id)
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return db_prompt

from pydantic import BaseModel
from fastapi import FastAPI
import openai_api
from fastapi.encoders import jsonable_encoder
app = FastAPI()


class Prompt(BaseModel):
    query: str


@app.post("/prompt")
async def root(prompt: Prompt):
    response = openai_api.gpt_prompt(prompt.query)
    print(response)
    return jsonable_encoder(response)

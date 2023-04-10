from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import api.openai as OpenAI
app = FastAPI()


class Prompt(BaseModel):
    query: str


@app.post("/prompt")
async def root(prompt: Prompt):
    response = OpenAI.gpt_prompt(prompt.query)
    print(response)
    return jsonable_encoder(response)

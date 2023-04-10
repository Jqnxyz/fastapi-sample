from fastapi import APIRouter
from ..schemas.api import Prompt
from ..api import openai as OpenAI
from fastapi.encoders import jsonable_encoder
router = APIRouter()


@router.post("/prompt")
async def root(prompt: Prompt):
    response = OpenAI.gpt_prompt(prompt.query)
    print(response)
    return jsonable_encoder(response)

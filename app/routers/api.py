from fastapi import APIRouter
from ..schemas.api import Prompt
from ..api import openai as OpenAI
router = APIRouter()


@router.post("/prompt")
async def root(prompt: Prompt):
    response = OpenAI.gpt_prompt(prompt.query)
    print(response.response)
    return response

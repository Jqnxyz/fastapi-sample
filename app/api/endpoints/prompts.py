from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.core import openai_api as OpenAI
from app.models import Prompt
from app.schemas.requests import PromptCreateRequest
from app.schemas.responses import PromptResponse

router = APIRouter()


# @router.get("/prompt", response_model=PromptResponse)
# async def read_prompt(
#     current_user: User = Depends(deps.get_current_user),
# ):
#     """Get current user"""
#     return current_user


@router.post("/prompt", response_model=PromptResponse)
async def create_prompt(
    prompt: PromptCreateRequest,
    session: AsyncSession = Depends(deps.get_session),
):
    response = OpenAI.gpt_prompt(prompt.query)

    """Create new prompt"""
    prompt = Prompt(query=prompt.query, response=response.response)

    session.add(prompt)
    await session.commit()
    return prompt

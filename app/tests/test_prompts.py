from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.main import app
from app.models import Prompt

import openai


async def test_create_prompt(
    client: AsyncClient, session: AsyncSession, monkeypatch
):
    def mock_completion_create(*args, **kwargs):
        return {
            'choices': [{
                'message': {
                    'role': 'assistant',
                    'content': 'Hello Test'},
                'finish_reason': 'stop',
                'index': 0
            }]
        }

    monkeypatch.setattr(openai.ChatCompletion, "create",
                        mock_completion_create)

    expected_query = "This is a prompt query."
    response = await client.post(
        app.url_path_for("create_prompt"),
        json={
            "query": expected_query
        },
    )
    assert response.status_code == 200
    result = await session.execute(select(Prompt).where(Prompt.query == expected_query))
    prompt = result.scalars().first()
    assert prompt is not None
    assert prompt.response == "Hello Test"

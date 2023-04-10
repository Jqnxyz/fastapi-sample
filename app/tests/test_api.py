from fastapi.testclient import TestClient
from app.main import app
from app.sql_app.models import Prompt
from app.sql_app.database import SessionLocal
import openai
client = TestClient(app)
db = SessionLocal()


def test_post_prompt(monkeypatch):
    # Mock OpenAI
    def mock_completion_create(*args, **kwargs):
        return {
            'choices': [{
                'message': {
                    'role': 'assistant',
                    'content': 'The test is working.'},
                'finish_reason': 'stop',
                'index': 0
            }]
        }

    monkeypatch.setattr(openai.ChatCompletion, "create",
                        mock_completion_create)

    query = "Respond to this with nothing else except the phrase \"The test is working.\""
    response = client.post(
        "/prompt", json={"query": query})

    assert response.status_code == 400
    assert response.json() == {"query": query,
                               "response": "The test is working."}
    assert db.query(Prompt).first().prompt == query

from fastapi.testclient import TestClient
from app.main import app
from app.schemas.api import PromptResponse
client = TestClient(app)


def test_post_prompt(mocker):
    # Mock OpenAI
    expected_response = PromptResponse(
        query="Respond to this with nothing else except the phrase \"The test is working.\"", response="The test is working.")

    mocker.patch("app.api.openai.gpt_prompt",
                 return_value=expected_response)

    query = "Respond to this with nothing else except the phrase \"The test is working.\""
    response = client.post(
        "/prompt", json={"query": query})
    assert response.status_code == 200
    assert response.json() == {"query": query,
                               "response": "The test is working."}

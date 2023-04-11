import openai

from app.core import config

from ..schemas.openai_api import GptResponse

openai.organization = config.settings.OPENAI_ORG
openai.api_key = config.settings.OPENAI_API_KEY


def list_models():
    return openai.Engine.list()


def gpt_prompt(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    message = completion.get("choices")[0].get("message").get("content")
    return GptResponse(query=prompt, response=message)

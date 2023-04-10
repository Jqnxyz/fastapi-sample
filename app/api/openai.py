import os
import openai
from ..schemas.api import PromptResponse
openai.organization = "org-WHgcvG5yviJ87v8Exr3GDihS"
openai.api_key = os.getenv("OPENAI_API_KEY")


def list_models():
    return openai.Engine.list()


def gpt_prompt(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    message = completion.get("choices")[0].get("message").get("content")
    return PromptResponse(query=prompt, response=message)

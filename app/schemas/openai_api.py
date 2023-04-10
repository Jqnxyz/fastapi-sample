from pydantic import BaseModel


class BaseRequest(BaseModel):
    # may define additional fields or config shared across requests
    pass


class GptResponse(BaseModel):
    query: str
    response: str

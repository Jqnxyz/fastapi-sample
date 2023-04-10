from sqlalchemy import Column, Integer, Text

from ..database import Base


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text)
